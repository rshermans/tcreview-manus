import pytest
import sys
import os
from unittest.mock import MagicMock

# Set SECRET_KEY to avoid ValueError in Config
os.environ["SECRET_KEY"] = "test_secret_key"

# Mock external dependencies that might be missing
sys.modules["requests"] = MagicMock()
sys.modules["dotenv"] = MagicMock()
sys.modules["flask"] = MagicMock()
sys.modules["flask_cors"] = MagicMock()

# Add the backend directory to sys.path to allow importing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now we can import the service
from services.llm_service import final_evaluation

def test_final_evaluation_happy_path():
    """Test standard valid inputs for final_evaluation."""
    user_perception = {"trust": 80, "clarity": 90}
    ai_analysis = {"factual": 70, "logical": 80}

    # user_score = (80 + 90) / 2 = 85
    # ai_score = (70 + 80) / 2 = 75
    # final_score = (85 * 0.3) + (75 * 0.7) = 25.5 + 52.5 = 78

    result = final_evaluation(user_perception, ai_analysis)

    assert result["final_score"] == 78
    assert result["user_vs_ai_discrepancy"] == 10.0
    assert "summary" in result

def test_final_evaluation_empty_user_perception():
    """Test empty user perception dictionary. Should return 0 for user score."""
    user_perception = {}
    ai_analysis = {"factual": 70, "logical": 80}

    # ai_score = 75
    # user_score = 0
    # final_score = 75 * 0.7 = 52.5 -> round to even (52)

    result = final_evaluation(user_perception, ai_analysis)
    assert result["final_score"] == 52

def test_final_evaluation_empty_ai_analysis():
    """Test empty AI analysis dictionary. Should return 0 for AI score."""
    user_perception = {"trust": 80, "clarity": 90}
    ai_analysis = {}

    # user_score = 85
    # ai_score = 0
    # final_score = 85 * 0.3 = 25.5 -> round to even (26)

    result = final_evaluation(user_perception, ai_analysis)
    assert result["final_score"] == 26

def test_final_evaluation_non_numeric_input():
    """Test non-numeric inputs. Should ignore non-numeric values."""
    user_perception = {"trust": "high", "clarity": 90}
    ai_analysis = {"factual": 70, "logical": 80}

    # user_score = 90 (only one valid value)
    # ai_score = 75
    # final_score = (90 * 0.3) + (75 * 0.7) = 27 + 52.5 = 79.5 -> round to even (80)

    result = final_evaluation(user_perception, ai_analysis)
    assert result["final_score"] == 80
