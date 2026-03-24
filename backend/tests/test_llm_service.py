
import pytest
import os
import sys

# Add backend to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set dummy secret key to bypass Config check during import
os.environ['SECRET_KEY'] = 'dummy_secret_key'

from services.llm_service import analyze_content, final_evaluation
from config import Config

def test_analyze_content_mock(monkeypatch):
    """Test analyze_content returns mock data when API key is missing/invalid."""
    # Ensure API key is invalid/placeholder
    monkeypatch.setattr(Config, "LLM_API_KEY", "sua_chave_api_llm")

    result = analyze_content("text", "test content")

    assert isinstance(result, dict)
    assert "analysis" in result
    assert "sourceReliability" in result
    assert isinstance(result["sourceReliability"], int)
    # Check fallback values matching the mock return
    assert result["sourceReliability"] == 60

def test_final_evaluation_mixed_types():
    """Test final_evaluation handles mixed types in input dicts."""
    user_perception = {"score": 80, "comment": "Good"}
    ai_analysis = {
        "analysis": "Some text",
        "sourceReliability": 60,
        "factualConsistency": 70
    }

    result = final_evaluation(user_perception, ai_analysis)

    assert isinstance(result, dict)
    assert "final_score" in result
    # user_score = 80 (comment ignored)
    # ai_score = (60+70)/2 = 65
    # final = 80*0.3 + 65*0.7 = 24 + 45.5 = 69.5 -> round -> 70 (or 69 depending on rounding)
    # round(69.5) in Python 3 rounds to nearest even number -> 70
    expected_score = round(80 * 0.3 + 65 * 0.7)
    assert result["final_score"] == expected_score

def test_final_evaluation_empty():
    """Test final_evaluation handles empty inputs gracefully."""
    result = final_evaluation({}, {})
    assert result["final_score"] == 0

def test_analyze_content_api_success(monkeypatch):
    """Test analyze_content successfully calls API and parses response."""
    monkeypatch.setattr(Config, "LLM_API_KEY", "real_key")

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {
                "choices": [{
                    "message": {
                        "content": '{"analysis": "test", "sourceReliability": 80, "factualConsistency": 80, "contentQuality": 80, "technicalIntegrity": 80}'
                    }
                }]
            }

    def mock_post(*args, **kwargs):
        return MockResponse()

    # Mock requests.post
    monkeypatch.setattr("services.llm_service.requests.post", mock_post)

    result = analyze_content("text", "content")
    assert result["sourceReliability"] == 80
    assert result["analysis"] == "test"

def test_analyze_content_api_invalid_json_structure(monkeypatch):
    """Test analyze_content handles non-dict JSON response from LLM."""
    monkeypatch.setattr(Config, "LLM_API_KEY", "real_key")

    class MockResponse:
        def raise_for_status(self):
            pass
        def json(self):
            return {
                "choices": [{
                    "message": {
                        "content": '["list", "instead", "of", "dict"]'
                    }
                }]
            }

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("services.llm_service.requests.post", mock_post)

    result = analyze_content("text", "content")
    # It should fall back to returning the raw text as analysis
    assert result["analysis"] == '["list", "instead", "of", "dict"]'
    assert result["sourceReliability"] == 50
