"""Configuration for Vnstock API client."""

import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class APIConfig:
    """Configuration for API endpoints."""
    base_url: str
    username: Optional[str] = None
    password: Optional[str] = None
    timeout: float = 30.0

# API configuration
DEFAULT_CONFIG = APIConfig(
    base_url="http://72.60.233.159:8002",
    username=os.getenv("VNSTOCK_USERNAME"),
    password=os.getenv("VNSTOCK_PASSWORD"),
    timeout=30.0
)
