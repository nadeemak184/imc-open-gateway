import pytest
import httpx
from app.modules.verifier import verify_number

@pytest.mark.asyncio
async def test_verify_number_success(monkeypatch):
    class FakeResp:
        def __init__(self):
            self._json = {"valid": True, "operatorName": "TestOp"}
        def raise_for_status(self): pass
        def json(self): return self._json

    async def fake_post(self, path, body):
        return {"valid": True, "operatorName": "TestOp", "other": "meta"}

    monkeypatch.setattr("app.modules.providers.open_gateway.OpenGatewayClient._post", fake_post)
    result = await verify_number("+911234567890")
    assert result["valid"] is True
    assert result["provider"] == "TestOp"
