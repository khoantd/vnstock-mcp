# API Reference - Complete List of All Called APIs

This document lists all API endpoints used in the Next.js Blog CMS application, organized by category.

## Table of Contents
1. [Next.js API Routes (Frontend → Backend Proxy)](#nextjs-api-routes)
2. [Backend API Endpoints](#backend-api-endpoints)
3. [External APIs](#external-apis)
4. [NextAuth APIs](#nextauth-apis)
5. [Vnstock API Endpoints](#vnstock-api-endpoints)

---

## Next.js API Routes

These are Next.js API routes that act as proxies to the backend API. All routes use `serverApiRequestWithCookies()` to forward requests with authentication cookies.

### Authentication APIs

#### `POST /api/auth/register`
- **Purpose**: Register a new user
- **Proxy To**: Backend `/api/auth/register`
- **File**: `app/api/auth/register/route.ts`

#### `GET /api/auth/[...nextauth]`
- **Purpose**: NextAuth.js authentication endpoints
- **Includes**: `/api/auth/signin`, `/api/auth/callback/google`, `/api/auth/signout`, etc.
- **File**: `app/api/auth/[...nextauth]/route.ts`

### Stock Analysis APIs

#### `GET /api/stock-analyses`
- **Purpose**: List all stock analyses (with pagination)
- **Query Params**: `page`, `limit`, `symbol`, `status`, `favorite`
- **Proxy To**: Backend `/api/stock-analyses`
- **File**: `app/api/stock-analyses/route.ts`

#### `POST /api/stock-analyses`
- **Purpose**: Create a new stock analysis
- **Body**: `{ symbol, name?, csvContent, minPctChange? }`
- **Proxy To**: Backend `/api/stock-analyses`
- **File**: `app/api/stock-analyses/route.ts`

#### `GET /api/stock-analyses/[id]`
- **Purpose**: Get a single stock analysis by ID
- **Query Params**: `excludeData` (optional)
- **Proxy To**: Backend `/api/stock-analyses/[id]`
- **File**: `app/api/stock-analyses/[id]/route.ts`

#### `PATCH /api/stock-analyses/[id]`
- **Purpose**: Update a stock analysis
- **Body**: Partial update object
- **Proxy To**: Backend `/api/stock-analyses/[id]`
- **File**: `app/api/stock-analyses/[id]/route.ts`

#### `DELETE /api/stock-analyses/[id]`
- **Purpose**: Delete a stock analysis
- **Proxy To**: Backend `/api/stock-analyses/[id]`
- **File**: `app/api/stock-analyses/[id]/route.ts`

#### `POST /api/stock-analyses/[id]/upload`
- **Purpose**: Upload CSV file for a stock analysis
- **Body**: FormData with CSV file
- **Proxy To**: Backend `/api/stock-analyses/[id]/upload`
- **File**: `app/api/stock-analyses/[id]/upload/route.ts`

#### `POST /api/stock-analyses/[id]/import`
- **Purpose**: Import stock data
- **Proxy To**: Backend `/api/stock-analyses/[id]/import`
- **File**: `app/api/stock-analyses/[id]/import/route.ts`

#### `POST /api/stock-analyses/[id]/supplement`
- **Purpose**: Supplement stock analysis data
- **Proxy To**: Backend `/api/stock-analyses/[id]/supplement`
- **File**: `app/api/stock-analyses/[id]/supplement/route.ts`

#### `POST /api/stock-analyses/[id]/analyze`
- **Purpose**: Trigger factor analysis for a stock analysis
- **Proxy To**: Backend `/api/stock-analyses/[id]/analyze`
- **File**: `app/api/stock-analyses/[id]/analyze/route.ts`

#### `GET /api/stock-analyses/[id]/status`
- **Purpose**: Get analysis status (for real-time updates)
- **Proxy To**: Backend `/api/stock-analyses/[id]/status`
- **File**: `app/api/stock-analyses/[id]/status/route.ts`

#### `GET /api/stock-analyses/[id]/daily-factor-data`
- **Purpose**: Get daily factor data with pagination
- **Query Params**: `page`, `limit`, `orderBy`, `order`
- **Proxy To**: Backend `/api/stock-analyses/[id]/daily-factor-data`
- **File**: `app/api/stock-analyses/[id]/daily-factor-data/route.ts`

#### `GET /api/stock-analyses/[id]/daily-scores`
- **Purpose**: Get daily scoring data with pagination
- **Query Params**: `page`, `limit`, `orderBy`, `order`
- **Proxy To**: Backend `/api/stock-analyses/[id]/daily-scores`
- **File**: `app/api/stock-analyses/[id]/daily-scores/route.ts`

#### `GET /api/stock-analyses/[id]/predictions`
- **Purpose**: Get predictions with sorting
- **Query Params**: `orderBy`, `order`
- **Proxy To**: Backend `/api/stock-analyses/[id]/predictions`
- **File**: `app/api/stock-analyses/[id]/predictions/route.ts`

#### `POST /api/stock-analyses/delete-all`
- **Purpose**: Delete all stock analyses (admin only)
- **Proxy To**: Backend `/api/stock-analyses` (DELETE operations)
- **File**: `app/api/stock-analyses/delete-all/route.ts`

### Earnings APIs

#### `GET /api/earnings`
- **Purpose**: List earnings data
- **Query Params**: `symbol`, `limit`, `page`
- **Proxy To**: Backend `/api/earnings`
- **File**: `app/api/earnings/route.ts`

#### `GET /api/earnings/[symbol]`
- **Purpose**: Get earnings data for a specific symbol
- **Proxy To**: Backend `/api/earnings/[symbol]`
- **File**: `app/api/earnings/route.ts` (handled via query param)

#### `POST /api/earnings/analyze`
- **Purpose**: Trigger AI analysis of earnings data
- **Body**: `{ symbols?: string[], earningsIds?: number[] }`
- **Proxy To**: Backend `/api/earnings/analyze`
- **File**: `app/api/earnings/analyze/route.ts`

### Stock Price APIs

#### `GET /api/stock-price/[symbol]`
- **Purpose**: Get current stock price
- **Query Params**: `country` (US | VN)
- **Proxy To**: Vnstock API (for VN stocks) or Backend API (for US stocks)
- **File**: `app/api/stock-price/[symbol]/route.ts`

### User APIs

#### `GET /api/users/by-email`
- **Purpose**: Get user by email address
- **Query Params**: `email`
- **Proxy To**: Backend `/api/users/by-email`
- **File**: `app/api/users/by-email/route.ts`

### Vnstock API Proxies

#### `POST /api/vnstock/auth/login`
- **Purpose**: Login to Vnstock API
- **Proxy To**: Vnstock API `/api/v1/auth/login`
- **File**: `app/api/vnstock/auth/login/route.ts`

#### `POST /api/vnstock/auth/register`
- **Purpose**: Register with Vnstock API
- **Proxy To**: Vnstock API `/api/v1/auth/register`
- **File**: `app/api/vnstock/auth/register/route.ts`

#### `GET /api/vnstock/auth/me`
- **Purpose**: Get current Vnstock user
- **Proxy To**: Vnstock API `/api/v1/auth/me`
- **File**: `app/api/vnstock/auth/me/route.ts`

#### `POST /api/vnstock/auth/logout`
- **Purpose**: Logout from Vnstock API
- **Proxy To**: Vnstock API `/api/v1/auth/logout`
- **File**: `app/api/vnstock/auth/logout/route.ts`

#### `POST /api/vnstock/company/[endpoint]`
- **Purpose**: Proxy for company information endpoints
- **Endpoints**: `overview`, `shareholders`, `officers`, `subsidiaries`, `affiliate`, `news`, `events`
- **Proxy To**: Vnstock API `/api/v1/company/[endpoint]`
- **File**: `app/api/vnstock/company/[endpoint]/route.ts`

#### `POST /api/vnstock/financial/[endpoint]`
- **Purpose**: Proxy for financial data endpoints
- **Endpoints**: `balance-sheet`, `income-statement`, `cash-flow`, `ratios`
- **Proxy To**: Vnstock API `/api/v1/financial/[endpoint]`
- **File**: `app/api/vnstock/financial/[endpoint]/route.ts`

#### `POST /api/vnstock/trading/[endpoint]`
- **Purpose**: Proxy for trading data endpoints
- **Endpoints**: `stats`, `side-stats`, `price-board`, `price-history`, `foreign-trade`, `prop-trade`, `insider-deal`, `order-stats`
- **Proxy To**: Vnstock API `/api/v1/trading/[endpoint]`
- **File**: `app/api/vnstock/trading/[endpoint]/route.ts`

#### `POST /api/vnstock/download/[endpoint]`
- **Purpose**: Proxy for CSV download endpoints
- **Endpoints**: `csv`, `multiple`
- **Proxy To**: Vnstock API `/api/v1/download/[endpoint]`
- **File**: `app/api/vnstock/download/[endpoint]/route.ts`

### Debug APIs

#### `GET /api/debug/env`
- **Purpose**: Debug environment variables (development only)
- **File**: `app/api/debug/env/route.ts`

#### `GET /api/debug/session`
- **Purpose**: Debug session information (development only)
- **File**: `app/api/debug/session/route.ts`

---

## Backend API Endpoints

These are the backend API endpoints (default: `http://72.60.233.159:3050`) that are called via Next.js API route proxies.

### Base URL
- **Default**: `http://72.60.233.159:3050`
- **Configurable**: `NEXT_PUBLIC_API_URL` environment variable
- **Helper**: `API_CONFIG.BASE_URL` from `lib/api-config.ts`

### Stock Analysis Endpoints

- `GET /api/stock-analyses` - List stock analyses
- `POST /api/stock-analyses` - Create stock analysis
- `GET /api/stock-analyses/[id]` - Get single analysis
- `PATCH /api/stock-analyses/[id]` - Update analysis
- `DELETE /api/stock-analyses/[id]` - Delete analysis
- `POST /api/stock-analyses/[id]/upload` - Upload CSV
- `POST /api/stock-analyses/[id]/import` - Import data
- `POST /api/stock-analyses/[id]/supplement` - Supplement data
- `POST /api/stock-analyses/[id]/analyze` - Trigger factor analysis
- `GET /api/stock-analyses/[id]/status` - Get analysis status
- `GET /api/stock-analyses/[id]/daily-factor-data` - Get daily factor data
- `GET /api/stock-analyses/[id]/daily-scores` - Get daily scores
- `GET /api/stock-analyses/[id]/predictions` - Get predictions

### Earnings Endpoints

- `GET /api/earnings` - List earnings
- `GET /api/earnings/[symbol]` - Get earnings by symbol
- `POST /api/earnings/sync` - Sync earnings from Alpha Vantage
- `POST /api/earnings/analyze` - Trigger AI analysis

### User Endpoints

- `GET /api/users/by-email` - Get user by email
- `POST /api/auth/login` - Backend login (if used)
- `POST /api/auth/register` - Backend registration (if used)

---

## External APIs

### Alpha Vantage API

**Base URL**: `https://www.alphavantage.co/query`

#### `GET /query?function=EARNINGS&symbol={symbol}&apikey={key}`
- **Purpose**: Fetch earnings data for a stock symbol
- **Service**: `lib/earnings-service.ts`
- **Rate Limits**: 5 calls/minute, 500 calls/day
- **API Key**: `ALPHA_VANTAGE_API_KEY` environment variable
- **Usage**: Used by backend to fetch earnings data

**Example**:
```typescript
const response = await axios.get('https://www.alphavantage.co/query', {
  params: {
    function: 'EARNINGS',
    symbol: 'AAPL',
    apikey: process.env.ALPHA_VANTAGE_API_KEY
  }
});
```

### LiteLLM API

**Base URL**: Configurable via `LITELLM_BASE_URL` (default: `http://khoadue.me:4010`)

#### `POST /v1/chat/completions`
- **Purpose**: AI chat completions for earnings analysis and price recommendations
- **Service**: `lib/litellm-proxy.ts` (optional wrapper)
- **Direct Usage**: Backend uses `litellm` package directly
- **API Key**: `LITELLM_API_KEY` environment variable
- **Headers**: `Authorization: Bearer {LITELLM_API_KEY}`
- **Body**: Standard OpenAI-compatible chat completion format

**Example**:
```typescript
const response = await fetch(`${baseUrl}/v1/chat/completions`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`
  },
  body: JSON.stringify({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: prompt }],
    temperature: 0.3,
    max_tokens: 1000
  })
});
```

**Note**: The backend uses the `litellm` package directly, not the proxy wrapper.

### Vnstock API

**Base URL**: `http://72.60.233.159:8002` (configurable via `NEXT_PUBLIC_VNSTOCK_API_URL`)

#### Authentication Endpoints
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/auth/register` - Register
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/logout` - Logout

#### Company Endpoints
- `POST /api/v1/company/overview` - Company overview
- `POST /api/v1/company/shareholders` - Shareholders
- `POST /api/v1/company/officers` - Officers
- `POST /api/v1/company/subsidiaries` - Subsidiaries
- `POST /api/v1/company/affiliate` - Affiliate companies
- `POST /api/v1/company/news` - Company news
- `POST /api/v1/company/events` - Company events

#### Financial Endpoints
- `POST /api/v1/financial/balance-sheet` - Balance sheet
- `POST /api/v1/financial/income-statement` - Income statement
- `POST /api/v1/financial/cash-flow` - Cash flow
- `POST /api/v1/financial/ratios` - Financial ratios

#### Trading Endpoints
- `POST /api/v1/trading/stats` - Trading statistics
- `POST /api/v1/trading/side-stats` - Side statistics
- `POST /api/v1/trading/price-board` - Price board (real-time prices)
- `POST /api/v1/trading/price-history` - Price history
- `POST /api/v1/trading/foreign-trade` - Foreign trade data
- `POST /api/v1/trading/prop-trade` - Proprietary trading
- `POST /api/v1/trading/insider-deal` - Insider deals
- `POST /api/v1/trading/order-stats` - Order statistics

#### Download Endpoints
- `POST /api/v1/download/csv` - Download single CSV
- `POST /api/v1/download/multiple` - Download multiple CSVs

**Service**: `lib/vnstock-api.ts` (client-side service)
**Authentication**: Token-based (stored in cookies)
**Proxy**: All requests go through Next.js API routes

---

## NextAuth APIs

NextAuth.js provides the following authentication endpoints automatically:

- `GET /api/auth/signin` - Sign in page
- `POST /api/auth/signin` - Sign in handler
- `GET /api/auth/signout` - Sign out handler
- `GET /api/auth/callback/google` - Google OAuth callback
- `GET /api/auth/session` - Get current session
- `GET /api/auth/csrf` - Get CSRF token
- `GET /api/auth/providers` - List available providers

**Configuration**: `lib/auth.ts`
**Provider**: Google OAuth
**Session Storage**: Database (Prisma adapter)

---

## API Request Patterns

### Frontend → Next.js API Route → Backend

**Pattern**:
```typescript
// Frontend component
const response = await fetch('/api/stock-analyses', {
  credentials: 'include'
});

// Next.js API route (app/api/stock-analyses/route.ts)
const data = await serverApiRequestWithCookies(
  '/api/stock-analyses',
  request
);

// Backend API (http://72.60.233.159:3050/api/stock-analyses)
```

### Direct External API Calls

**Pattern**:
```typescript
// Alpha Vantage (backend only)
const response = await axios.get('https://www.alphavantage.co/query', {
  params: { function: 'EARNINGS', symbol, apikey }
});

// LiteLLM (backend only)
const response = await completion({
  model: 'gpt-4o-mini',
  messages: [{ role: 'user', content: prompt }]
});
```

### Vnstock API Calls

**Pattern**:
```typescript
// Client-side service
const vnstockApi = new VnstockApiService();
const data = await vnstockApi.getPriceBoard({ symbols_list: ['VIC'] });

// Goes through Next.js proxy
// POST /api/vnstock/trading/price-board
// → Proxies to http://72.60.233.159:8002/api/v1/trading/price-board
```

---

## Environment Variables

### Required for APIs

- `NEXT_PUBLIC_API_URL` - Backend API URL (default: `http://72.60.233.159:3050`)
- `NEXT_PUBLIC_VNSTOCK_API_URL` - Vnstock API URL (default: `http://72.60.233.159:8002`)
- `ALPHA_VANTAGE_API_KEY` - Alpha Vantage API key
- `LITELLM_API_KEY` - LiteLLM API key
- `LITELLM_BASE_URL` - LiteLLM base URL (default: `http://khoadue.me:4010`)

### Authentication

- `GOOGLE_CLIENT_ID` - Google OAuth client ID
- `GOOGLE_CLIENT_SECRET` - Google OAuth client secret
- `NEXTAUTH_SECRET` - NextAuth.js secret
- `NEXTAUTH_URL` - NextAuth.js base URL

---

## API Helper Functions

### `serverApiRequestWithCookies()`
- **Location**: `lib/api-config.ts`
- **Purpose**: Server-side API requests with cookie forwarding
- **Usage**: Used in all Next.js API routes to proxy to backend

### `apiRequest()`
- **Location**: `lib/api-config.ts`
- **Purpose**: Client-side API requests to backend
- **Usage**: Direct backend API calls (less common)

### `fetcher()`
- **Location**: `lib/utils.ts`
- **Purpose**: SWR fetcher function
- **Usage**: Used with `useSWR` hook for data fetching

### `vnstockRequest()`
- **Location**: `lib/vnstock-api.ts`
- **Purpose**: Vnstock API request wrapper
- **Usage**: Internal helper for VnstockApiService

---

## Rate Limits & Best Practices

### Alpha Vantage
- **Limit**: 5 calls/minute, 500 calls/day
- **Practice**: 12-second delays between calls in `earnings-service.ts`

### LiteLLM
- **Limit**: Depends on provider configuration
- **Practice**: Error handling with retries

### Backend API
- **Limit**: None specified
- **Practice**: Cookie-based authentication, error handling

### Vnstock API
- **Limit**: Depends on Vnstock API configuration
- **Practice**: Token-based authentication, error handling

---

## Error Handling

All API calls include comprehensive error handling:

1. **Connection Errors**: Detected and reported with helpful messages
2. **HTTP Errors**: Status codes and error messages extracted
3. **JSON Parsing**: Graceful handling of non-JSON responses
4. **Network Errors**: Timeout and DNS error detection

**Error Pattern**:
```typescript
try {
  const response = await fetch(url);
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.message || error.error);
  }
  return await response.json();
} catch (error) {
  // Handle connection errors, network errors, etc.
  logError(error, { context: 'api-call' });
  throw error;
}
```

---

## Summary

- **Next.js API Routes**: 30+ routes that proxy to backend
- **Backend API Endpoints**: 15+ endpoints for stock analysis, earnings, users
- **External APIs**: Alpha Vantage, LiteLLM, Vnstock
- **Authentication**: NextAuth.js with Google OAuth
- **Pattern**: Frontend → Next.js API → Backend → Database
- **No Direct DB Access**: Frontend never accesses database directly
