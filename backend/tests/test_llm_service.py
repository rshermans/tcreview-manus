import sys
from unittest.mock import MagicMock
import os

# Mock external dependencies that might not be installed in the test environment
sys.modules["requests"] = MagicMock()

# Mock config module
mock_config = MagicMock()
mock_config.Config = MagicMock()
sys.modules["config"] = mock_config

# Add backend directory to sys.path to allow imports
# We need to add 'backend' to path so that 'from config import Config' works if it is in backend/
# But wait, llm_service does 'from config import Config'. If config.py is in backend/, then we need backend/ in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from backend.services.llm_service import final_evaluation

def test_final_evaluation_happy_path():
    user_perception = {"clarity": 8, "accuracy": 9}
    ai_analysis = {"factuality": 7, "bias": 8}

    # Expected user_score = (8+9)/2 = 8.5
    # Expected ai_score = (7+8)/2 = 7.5
    # Expected final_score = (8.5 * 0.3) + (7.5 * 0.7) = 2.55 + 5.25 = 7.8
    # Rounded: 8

    result = final_evaluation(user_perception, ai_analysis)

    assert result["final_score"] == 8
    assert "summary" in result
    assert "user_vs_ai_discrepancy" in result

def test_final_evaluation_non_numeric_values():
    user_perception = {"clarity": "high", "accuracy": 9}
    ai_analysis = {"factuality": 7, "bias": 8}

    with pytest.raises(ValueError, match="Values in user_perception and ai_analysis must be numeric"):
        final_evaluation(user_perception, ai_analysis)

def test_final_evaluation_empty_input():
    user_perception = {}
    ai_analysis = {"factuality": 7}

    with pytest.raises(ValueError, match="Input dictionaries cannot be empty"):
        final_evaluation(user_perception, ai_analysis)

    with pytest.raises(ValueError, match="Input dictionaries cannot be empty"):
        final_evaluation({"a": 1}, {})
