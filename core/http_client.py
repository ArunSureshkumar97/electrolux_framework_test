from __future__ import annotations

import requests
from requests import Response, Session

from config.config import BASE_URL, DEFAULT_HEADERS
from utils.logger import get_logger

logger = get_logger("http_client")


class HttpClient:
    def __init__(self, base_url: str = BASE_URL, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.session: Session = requests.Session()
        self.session.headers.update(headers or DEFAULT_HEADERS)

    def _build_url(self, endpoint: str) -> str:
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        return f"{self.base_url}{endpoint}"

    def request(self, method: str, endpoint: str, json: dict | None = None) -> Response:
        url = self._build_url(endpoint)
        logger.info("REQUEST -> method=%s url=%s payload=%s", method, url, json)

        response = self.session.request(
            method=method.upper(),
            url=url,
            json=json,
            timeout=30,
        )

        logger.info(
            "RESPONSE -> status=%s body=%s",
            response.status_code,
            response.text[:500],
        )
        return response
