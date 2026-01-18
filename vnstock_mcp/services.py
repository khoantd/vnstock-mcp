"""API service classes for Vnstock endpoints."""

from typing import List, Dict, Any, Optional
from .client import VnstockAPIClient
from .config import APIConfig


class VnstockService:
    """Service for interacting with Vnstock API."""
    
    def __init__(self, client: VnstockAPIClient):
        self.client = client
    
    async def get_available_symbols(self) -> List[str]:
        """Get list of available stock symbols."""
        return await self.client.get("/api/v1/symbols")

    async def get_company_overview(self, symbol: str) -> Dict[str, Any]:
        """Get company overview information."""
        payload = {"symbol": symbol}
        return await self.client.post("/api/v1/company/overview", json=payload)

    async def get_company_news(self, symbol: str) -> List[Dict[str, Any]]:
        """Get company news."""
        payload = {"symbol": symbol}
        return await self.client.post("/api/v1/company/news", json=payload)

    async def get_price_history(self, symbol: str, start: str, end: str, interval: str = "D") -> List[Dict[str, Any]]:
        """Get price history for a symbol."""
        payload = {
            "symbol": symbol,
            "start": start,
            "end": end,
            "interval": interval
        }
        return await self.client.post("/api/v1/trading/price-history", json=payload)

    async def get_financial_ratios(self, symbol: str) -> Dict[str, Any]:
        """Get financial ratio data."""
        payload = {"symbol": symbol}
        return await self.client.post("/api/v1/financial/ratios", json=payload)

    async def get_trading_stats(self, symbol: str, start: str, end: str) -> List[Dict[str, Any]]:
        """Get trading statistics."""
        payload = {
            "symbol": symbol,
            "start": start,
            "end": end
        }
        return await self.client.post("/api/v1/trading/stats", json=payload)


class VnstockServiceFactory:
    """Factory for creating Vnstock service instances."""
    
    def __init__(self, config: Optional[APIConfig] = None):
        self.config = config
        self._client: Optional[VnstockAPIClient] = None
    
    async def __aenter__(self):
        self._client = VnstockAPIClient(self.config)
        await self._client.__aenter__()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.__aexit__(exc_type, exc_val, exc_tb)
    
    @property
    def stock(self) -> VnstockService:
        if not self._client:
            raise RuntimeError("Factory must be used as async context manager")
        return VnstockService(self._client)
