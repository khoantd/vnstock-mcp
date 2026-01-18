"""Base API client for Vnstock HTTP requests."""

import httpx
from typing import Optional, Dict, Any
from .config import APIConfig, DEFAULT_CONFIG


class VnstockAPIClient:
    """Base client for making HTTP requests to Vnstock API."""
    
    def __init__(self, config: Optional[APIConfig] = None):
        """
        Initialize the API client.
        
        Args:
            config: API configuration. If None, uses DEFAULT_CONFIG.
        """
        self.config = config or DEFAULT_CONFIG
        self._client: Optional[httpx.AsyncClient] = None
        self._token: Optional[str] = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        self._client = httpx.AsyncClient(timeout=self.config.timeout)
        if self.config.username and self.config.password:
            await self._login()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()

    async def _login(self):
        """Authenticate and get JWT token."""
        if not self._client:
            return
        
        url = f"{self.config.base_url}/auth/login"
        payload = {
            "username": self.config.username,
            "password": self.config.password
        }
        response = await self._client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        self._token = data.get("access_token")

    def _get_headers(self, headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Combine default headers with custom headers and auth token."""
        all_headers = headers.copy() if headers else {}
        if self._token:
            all_headers["Authorization"] = f"Bearer {self._token}"
        return all_headers
    
    async def get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Any:
        """Make a GET request."""
        if not self._client:
            raise RuntimeError("Client must be used as async context manager")
        
        url = f"{self.config.base_url}{endpoint}"
        response = await self._client.get(url, params=params, headers=self._get_headers(headers))
        response.raise_for_status()
        return response.json()
    
    async def post(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Any:
        """Make a POST request."""
        if not self._client:
            raise RuntimeError("Client must be used as async context manager")
        
        url = f"{self.config.base_url}{endpoint}"
        response = await self._client.post(url, json=json, headers=self._get_headers(headers))
        response.raise_for_status()
        return response.json()
