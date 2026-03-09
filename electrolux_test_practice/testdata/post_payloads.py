from schemas.post_schema import CreatePostPayload

VALID_POST_PAYLOAD = CreatePostPayload(
    title="FRAMEWORK TEST",
    body="Validating maintainable pytest framework",
    userId=101,
)

ANOTHER_VALID_POST_PAYLOAD = CreatePostPayload(
    title="Another Post",
    body="Additional payload for test coverage",
    userId=55,
)

UPDATE_POST_PAYLOAD = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 99,
}
