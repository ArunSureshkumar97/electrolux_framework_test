from __future__ import annotations

import requests
from requests import Response, Session

from config import config as conf
from utils.logger import get_logger

logger = get_logger("http_client")


class HttpClient:
    def __init__(self, headers: dict | None = None):
        self.session: Session = requests.Session()
        self.session.headers.update(headers or conf.DEFAULT_HEADERS)

    def _build_url(self, endpoint: str) -> str:
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        return f"{conf.BASE_URL.rstrip('/')}{endpoint}"

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