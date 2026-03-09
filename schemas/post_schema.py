from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class BasePayload(BaseModel):
    model_config = ConfigDict(extra="forbid")
    endpoint: ClassVar[str]


class CreatePostPayload(BasePayload):
    endpoint: ClassVar[str] = "/posts"

    title: str
    body: str
    userId: int


class PostResponse(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class DeleteResponse(BaseModel):
    model_config = ConfigDict(extra="allow")
