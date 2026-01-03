from __future__ import annotations

import time
from typing import Any

import httpx

DEFAULT_BASE_URL = "https://www.goodreads.com"
DEFAULT_USER_AGENT = "goodreads-cli/0.1 (+https://github.com/)"


class GoodreadsClient:
    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        min_interval: float = 0.3,
        timeout: float = 10.0,
        cookies: dict[str, str] | None = None,
    ) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            headers={"User-Agent": DEFAULT_USER_AGENT},
            timeout=timeout,
            cookies=cookies,
        )
        self._min_interval = min_interval
        self._last_request = 0.0

    def _throttle(self) -> None:
        if self._min_interval <= 0:
            return
        now = time.monotonic()
        wait = self._min_interval - (now - self._last_request)
        if wait > 0:
            time.sleep(wait)
        self._last_request = time.monotonic()

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        self._throttle()
        response = self._client.get(path, params=params)
        response.raise_for_status()
        return response.json()

    def get_text(self, path: str, params: dict[str, Any] | None = None) -> str:
        self._throttle()
        response = self._client.get(path, params=params)
        response.raise_for_status()
        return response.text

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> GoodreadsClient:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
