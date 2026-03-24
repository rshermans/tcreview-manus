import pytest
import sys
import os

# Add the parent directory (backend) to sys.path so we can import services
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.llm_service import final_evaluation

def test_final_evaluation_happy_path():
    """Test standard case with populated dictionaries."""
    user_perception = {"metric1": 10, "metric2": 20}
    ai_analysis = {"metricA": 5, "metricB": 15}

    # user_score = (10+20)/2 = 15
    # ai_score = (5+15)/2 = 10
    # final = (15 * 0.3) + (10 * 0.7) = 4.5 + 7.0 = 11.5
    # round(11.5) -> 12 (round to nearest even number for .5 in Python 3? No, round(x) returns int. round(0.5)=0, round(1.5)=2. round(11.5) -> 12)

    result = final_evaluation(user_perception, ai_analysis)

    assert "final_score" in result
    assert result["final_score"] == 12
    assert "summary" in result
    assert "user_vs_ai_discrepancy" in result
    assert result["user_vs_ai_discrepancy"] == abs(15 - 10)

def test_final_evaluation_empty_user_perception():
    """Test with empty user perception dictionary."""
    user_perception = {}
    ai_analysis = {"metricA": 10}

    # Expectation: Should handle empty dict gracefully (e.g., treat as 0 or ignore)
    # Currently expected to fail with ZeroDivisionError
    try:
        result = final_evaluation(user_perception, ai_analysis)
        # If it doesn't raise, we assert reasonable behavior (to be defined by implementation)
        # For now, let's just ensure it returns a valid dict
        assert isinstance(result, dict)
    except ZeroDivisionError:
        pytest.fail("ZeroDivisionError raised for empty user_perception")

def test_final_evaluation_empty_ai_analysis():
    """Test with empty AI analysis dictionary."""
    user_perception = {"metric1": 10}
    ai_analysis = {}

    # Expectation: Should handle empty dict gracefully
    try:
        result = final_evaluation(user_perception, ai_analysis)
        assert isinstance(result, dict)
    except ZeroDivisionError:
        pytest.fail("ZeroDivisionError raised for empty ai_analysis")

def test_final_evaluation_both_empty():
    """Test with both dictionaries empty."""
    user_perception = {}
    ai_analysis = {}

    # Expectation: Should handle empty dicts gracefully
    try:
        result = final_evaluation(user_perception, ai_analysis)
        assert isinstance(result, dict)
        assert result["final_score"] == 0 # Logic might dictate 0 for no input
    except ZeroDivisionError:
        pytest.fail("ZeroDivisionError raised for empty inputs")
