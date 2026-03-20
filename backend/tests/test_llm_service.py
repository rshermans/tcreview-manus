import pytest
from services.llm_service import analyze_context

def test_analyze_context_structure():
    """Test that analyze_context returns the expected dictionary structure."""
    result = analyze_context("some content")
    assert isinstance(result, dict)
    assert "context_summary" in result
    assert "historical_context" in result
    assert "current_relevance" in result

def test_analyze_context_values():
    """Test that analyze_context returns non-empty strings for each key."""
    result = analyze_context("some content")
    assert isinstance(result["context_summary"], str)
    assert len(result["context_summary"]) > 0
    assert isinstance(result["historical_context"], str)
    assert len(result["historical_context"]) > 0
    assert isinstance(result["current_relevance"], str)
    assert len(result["current_relevance"]) > 0

def test_analyze_context_empty_input():
    """Test that analyze_context handles empty input string without error."""
    result = analyze_context("")
    assert isinstance(result, dict)
    # Check that keys still exist even with empty input
    assert "context_summary" in result
    assert "historical_context" in result
    assert "current_relevance" in result
