from fastmcp import FastMCP
import httpx
from vnstock_mcp.services import VnstockServiceFactory
from typing import Optional, List, Dict, Any

mcp = FastMCP("Vnstock MCP Server")

@mcp.tool()
async def get_symbols() -> str:
    """Get list of available stock symbols."""
    try:
        async with VnstockServiceFactory() as factory:
            symbols = await factory.stock.get_available_symbols()
            return f"Available symbols: {symbols}"
    except Exception as e:
        return f"Error fetching symbols: {str(e)}"

@mcp.tool()
async def get_company_overview(symbol: str) -> str:
    """Get overview for a specific company symbol."""
    try:
        async with VnstockServiceFactory() as factory:
            overview = await factory.stock.get_company_overview(symbol)
            return f"Company Overview for {symbol}: {overview}"
    except Exception as e:
        return f"Error fetching overview for {symbol}: {str(e)}"

@mcp.tool()
async def get_company_news(symbol: str) -> str:
    """Get news for a specific company symbol."""
    try:
        async with VnstockServiceFactory() as factory:
            news = await factory.stock.get_company_news(symbol)
            return f"News for {symbol}: {news}"
    except Exception as e:
        return f"Error fetching news for {symbol}: {str(e)}"

@mcp.tool()
async def get_price_history(symbol: str, start_date: str, end_date: str, interval: str = "D") -> str:
    """
    Get price history for a symbol.
    Args:
        symbol: Stock symbol (e.g., 'VNM')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        interval: Time interval ('D', 'W', 'M')
    """
    try:
        async with VnstockServiceFactory() as factory:
            history = await factory.stock.get_price_history(symbol, start_date, end_date, interval)
            return f"Price history for {symbol} from {start_date} to {end_date}: {history}"
    except Exception as e:
        return f"Error fetching price history for {symbol}: {str(e)}"

@mcp.tool()
async def get_financial_ratios(symbol: str) -> str:
    """Get financial ratios for a symbol."""
    try:
        async with VnstockServiceFactory() as factory:
            ratios = await factory.stock.get_financial_ratios(symbol)
            return f"Financial Ratios for {symbol}: {ratios}"
    except Exception as e:
        return f"Error fetching financial ratios for {symbol}: {str(e)}"

@mcp.tool()
async def get_trading_stats(symbol: str, start_date: str, end_date: str) -> str:
    """Get trading statistics for a symbol."""
    try:
        async with VnstockServiceFactory() as factory:
            stats = await factory.stock.get_trading_stats(symbol, start_date, end_date)
            return f"Trading stats for {symbol}: {stats}"
    except Exception as e:
        return f"Error fetching trading stats for {symbol}: {str(e)}"

if __name__ == "__main__":
    mcp.run()
