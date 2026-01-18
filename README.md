# Vnstock MCP Server

An MCP server to interact with the Vnstock Comprehensive API.

## Tools

- `get_symbols`: List available stock symbols.
- `get_company_overview`: Get basic info about a company.
- `get_company_news`: Get recent news for a company.
- `get_price_history`: Fetch historical price data.
- `get_financial_ratios`: Get key financial indicators.
- `get_trading_stats`: Get trading volume and statistics.

## Setup

1. Copy `.env.example` to `.env`.
2. Set `VNSTOCK_USERNAME` and `VNSTOCK_PASSWORD`.
3. Install dependencies: `pip install -e .`

## Running

```bash
python server.py
```
or using FastMCP:
```bash
fastmcp run server.py
```
