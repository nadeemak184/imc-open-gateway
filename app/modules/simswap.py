# simswap.py

from app.modules.providers.open_gateway import OpenGatewayClient

client = OpenGatewayClient()

async def check_simswap(number: str):
    resp = await client.sim_swap_check(number)
    # mapping example
    return {
        "number": number,
        "risk_score": resp.get("riskScore", 0.0),
        "reason": resp.get("reasonCode", "")
    }
