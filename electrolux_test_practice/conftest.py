import pytest

from handlers.api_handler import APIHandler
from testdata.post_payloads import VALID_POST_PAYLOAD


@pytest.fixture(scope="session")
def api_handler() -> APIHandler:
    return APIHandler()


@pytest.fixture()
def post_payload():
    return VALID_POST_PAYLOAD
