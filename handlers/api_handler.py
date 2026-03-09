from __future__ import annotations

from typing import Type

from pydantic import BaseModel
from requests import Response

from core.http_client import HttpClient
from schemas.post_schema import CreatePostPayload
from utils.logger import get_logger

logger = get_logger("api_handler")


class APIHandler:
    def __init__(self, client: HttpClient | None = None):
        self.client = client or HttpClient()

    def _validate_response_schema(
        self,
        response: Response,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        if validate_schema and response_model is not None and response.status_code < 300:
            response_model.model_validate(response.json())
            logger.info("Schema validation passed for model=%s", response_model.__name__)
        return response

    def create(
        self,
        payload: CreatePostPayload,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="POST",
            endpoint=payload.endpoint,
            json=payload.model_dump(),
        )
        return self._validate_response_schema(response, response_model, validate_schema)

    def post(
        self,
        endpoint: str,
        payload: dict,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="POST",
            endpoint=endpoint,
            json=payload,
        )
        return self._validate_response_schema(response, response_model, validate_schema)

    def put(
        self,
        endpoint: str,
        resource_id: int,
        payload: dict,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="PUT",
            endpoint=f"{endpoint.rstrip('/')}/{resource_id}",
            json=payload,
        )
        return self._validate_response_schema(response, response_model, validate_schema)

    def find(
        self,
        endpoint: str,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="GET",
            endpoint=endpoint,
        )
        return self._validate_response_schema(response, response_model, validate_schema)

    def find_by_id(
        self,
        endpoint: str,
        resource_id: int,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="GET",
            endpoint=f"{endpoint.rstrip('/')}/{resource_id}",
        )
        return self._validate_response_schema(response, response_model, validate_schema)

    def delete(
        self,
        endpoint: str,
        resource_id: int,
        response_model: Type[BaseModel] | None = None,
        validate_schema: bool = True,
    ) -> Response:
        response = self.client.request(
            method="DELETE",
            endpoint=f"{endpoint.rstrip('/')}/{resource_id}",
        )
        return self._validate_response_schema(response, response_model, validate_schema)