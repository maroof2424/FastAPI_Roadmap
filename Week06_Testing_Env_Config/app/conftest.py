import os
import pytest
from app.config import get_settings

@pytest.fixture(scope="session", autouse=True)
def load_test_env():
    os.environ["ENV"] = "test"
    settings = get_settings()
    return settings
