
from pathlib import Path

# Project locations
PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE_DIR = PROJECT_DIR.parent
REPOSITORY_PATH = WORKSPACE_DIR / "Python"

# AI model
MODEL_NAME = "qwen3:8b"

# Assignment issue
ISSUE_NUMBER = 15655
ISSUE_URL = "https://github.com/TheAlgorithms/Python/issues/15655"

# Agent permissions
MAX_TOOL_CALLS = 12
REQUIRE_EDIT_APPROVAL = True
