import pytest

from schemas.post_schema import DeleteResponse, PostResponse
from testdata.post_payloads import ANOTHER_VALID_POST_PAYLOAD, UPDATE_POST_PAYLOAD, VALID_POST_PAYLOAD

@pytest.mark.smoke
def test_get_all_posts(api_handler):
    response = api_handler.find("/posts", validate_schema=False)

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.regression
def test_get_post_by_id(api_handler):
    response = api_handler.find_by_id("/posts", 1, response_model=PostResponse)

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 1
    assert "title" in body
    assert "body" in body
    assert "userId" in body

@pytest.mark.regression
def test_create_post(api_handler):
    response = api_handler.create(VALID_POST_PAYLOAD, response_model=PostResponse)

    assert response.status_code == 201

    body = response.json()
    assert body["title"] == VALID_POST_PAYLOAD.title
    assert body["body"] == VALID_POST_PAYLOAD.body
    assert body["userId"] == VALID_POST_PAYLOAD.userId
    assert "id" in body

@pytest.mark.regression
def test_create_post_with_another_payload(api_handler):
    response = api_handler.create(
        ANOTHER_VALID_POST_PAYLOAD,
        response_model=PostResponse,
    )

    assert response.status_code == 201
    assert response.json()["title"] == ANOTHER_VALID_POST_PAYLOAD.title

@pytest.mark.regression
def test_update_post(api_handler):
    response = api_handler.put(
        endpoint="/posts",
        resource_id=1,
        payload=UPDATE_POST_PAYLOAD,
        response_model=PostResponse,
    )

    assert response.status_code == 200

    body = response.json()
    assert body["id"] == 1
    assert body["title"] == UPDATE_POST_PAYLOAD["title"]
    assert body["body"] == UPDATE_POST_PAYLOAD["body"]
    assert body["userId"] == UPDATE_POST_PAYLOAD["userId"]

@pytest.mark.regression
def test_delete_post(api_handler):
    response = api_handler.delete("/posts", 1, response_model=DeleteResponse)

    assert response.status_code == 200
    assert response.json() == {}

@pytest.mark.regression
def test_get_invalid_post_id_negative(api_handler):
    response = api_handler.find_by_id("/posts", 999999, validate_schema=False)

    assert response.status_code == 404
    assert response.json() == {}
