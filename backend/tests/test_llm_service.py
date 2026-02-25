import pytest
import unittest.mock as mock
from services.llm_service import analyze_content

def test_analyze_content_returns_dict():
    """Test that analyze_content returns a dictionary with expected keys."""
    result = analyze_content("text", "This is a test content")
    assert isinstance(result, dict)
    expected_keys = {"analysis", "sourceReliability", "factualConsistency", "contentQuality", "technicalIntegrity"}
    assert all(key in result for key in expected_keys)

def test_analyze_content_caching():
    """Test that analyze_content caching works by comparing timing."""
    import time
    content_type = "text"
    content = "Unique content for caching test"

    # First call (should populate cache)
    start_time = time.time()
    result1 = analyze_content(content_type, content)
    duration1 = time.time() - start_time

    # Second call (should be served from cache)
    start_time = time.time()
    result2 = analyze_content(content_type, content)
    duration2 = time.time() - start_time

    assert result1 == result2
    # Caching should be significantly faster
    assert duration2 < duration1

def test_analyze_content_cache_poisoning_protection():
    """Test that modifying the returned dict does not affect the cache."""
    content_type = "text"
    content = "Poisoning test content"

    result1 = analyze_content(content_type, content)
    original_value = result1["analysis"]
    result1["analysis"] = "MODIFIED"

    result2 = analyze_content(content_type, content)
    assert result2["analysis"] == original_value
    assert result2["analysis"] != "MODIFIED"

def test_analyze_content_does_not_cache_errors():
    """Test that transient errors are not cached."""
    content_type = "text"
    content = "Error caching test"

    # Clear cache for this test to ensure clean state
    from services.llm_service import _get_llm_analysis
    _get_llm_analysis.cache_clear()

    with mock.patch('services.llm_service.requests.post') as mock_post:
        with mock.patch('services.llm_service.Config') as mock_config:
            mock_config.LLM_API_KEY = "real_key_for_test"
            mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

            # 1. First call fails with a transient error
            mock_post.side_effect = Exception("Transient error")
            result1 = analyze_content(content_type, content)
            assert "Erro ao processar análise" in result1["analysis"]

            # 2. Second call should retry and succeed
            mock_post.side_effect = None
            mock_post.return_value.json.return_value = {
                "choices": [{"message": {"content": "Success after error"}}]
            }
            mock_post.return_value.raise_for_status.return_value = None

            result2 = analyze_content(content_type, content)
            assert result2["analysis"] == "Success after error"

            # 3. Third call should be cached
            mock_post.return_value.json.return_value = {
                "choices": [{"message": {"content": "Should not be called again"}}]
            }
            result3 = analyze_content(content_type, content)
            assert result3["analysis"] == "Success after error"
            assert mock_post.call_count == 2 # Once for failure, once for success
