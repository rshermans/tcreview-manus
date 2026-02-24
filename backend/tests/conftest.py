import os
import sys
from unittest.mock import MagicMock

# Set necessary environment variables BEFORE any imports that rely on them
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['LLM_API_KEY'] = 'test_llm_key'

# Mock missing modules to allow imports
# These mocks must be set before any other imports that might use them
sys.modules['requests'] = MagicMock()
sys.modules['dotenv'] = MagicMock()
# No need to explicitly mock load_dotenv as MagicMock handles attributes automatically

import pytest

# Add backend directory to sys.path so that modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
