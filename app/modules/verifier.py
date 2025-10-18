# verifier.py

from typing import Dict
from app.modules.providers.open_gateway import OpenGatewayClient
from app.core.config import settings

client = OpenGatewayClient()

async def verify_number(number: str) -> Dict:
    # call real API
    resp = await client.verify_number(number)
    # transform provider response into your internal model
    # Example mapping (adjust keys based on real API)
    return {
        "number": number,
        "valid": resp.get("valid", False),
        "provider": resp.get("operatorName", "unknown"),
        "meta": resp
    }
