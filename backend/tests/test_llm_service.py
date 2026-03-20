import pytest
from services.llm_service import cross_verify_content

def test_cross_verify_content_structure():
    """
    Test that cross_verify_content returns a dictionary with the expected keys.
    """
    content = "Some dummy content"
    analysis = {"some": "analysis"}

    result = cross_verify_content(content, analysis)

    assert isinstance(result, dict)
    assert "cross_verification_summary" in result
    assert "verified_sources" in result
    assert "confidence_score" in result

def test_cross_verify_content_values():
    """
    Test that cross_verify_content returns values of correct types.
    """
    content = "Some dummy content"
    analysis = {"some": "analysis"}

    result = cross_verify_content(content, analysis)

    assert isinstance(result["cross_verification_summary"], str)
    assert isinstance(result["verified_sources"], list)
    assert isinstance(result["confidence_score"], (int, float))

    # Check if list contains strings
    if result["verified_sources"]:
        assert all(isinstance(source, str) for source in result["verified_sources"])
