
# simswap.py
# Basic heuristic for sim swap detection. In production, combine device history, operator signals and fraud feeds.

async def check_simswap(number: str):
    # Mock implementation: random-ish deterministic score based on digits
    digits = [ord(c) for c in number if c.isdigit()]
    score = (sum(digits) % 100) / 100.0
    reason = "mock heuristic score; integrate with real telecom risk signals"
    return {"number": number, "risk_score": score, "reason": reason}
