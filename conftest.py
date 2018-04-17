import pytest
from main import create_lunchbot

# we need to create our fixtures here for the tests to pick them up, that
# was our problem!
@pytest.fixture
def app():
    return create_lunchbot()
