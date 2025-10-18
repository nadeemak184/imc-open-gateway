# backend/app/modules/providers/open_gateway.py

import httpx
from app.core.config import settings
from typing import Dict, Any

class OpenGatewayClient:
    def __init__(self):
        self.base = settings.OPEN_GATEWAY_BASE_URL
        self.api_key = settings.OPEN_GATEWAY_API_KEY
        self.timeout = settings.REQUEST_TIMEOUT

    async def _post(self, path: str, body: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base.rstrip('/')}/{path.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.post(url, json=body, headers=headers)
        resp.raise_for_status()
        return resp.json()

    async def verify_number(self, number: str) -> Dict[str, Any]:
        # path depends on operator’s API spec
        body = {"msisdn": number}
        result = await self._post("/number-verification/v1/check", body)
        return result

    async def sim_swap_check(self, number: str) -> Dict[str, Any]:
        body = {"msisdn": number}
        result = await self._post("/simswap/v1/check", body)
        return result

    async def device_location(self, number: str) -> Dict[str, Any]:
        body = {"msisdn": number}
        result = await self._post("/location/v1/query", body)
        return result
