import pytest
from handlers.api_handler import APIHandler

@pytest.fixture(scope="session")
def api_handler() -> APIHandler:
    print('wdwd')
    yield APIHandler()
    print('ewfdefde')