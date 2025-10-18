
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.modules import verifier

router = APIRouter()

class VerifyRequest(BaseModel):
    number: str

class VerifyResponse(BaseModel):
    number: str
    valid: bool
    provider: str
    meta: dict = {}

@router.post("/", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    try:
        result = await verifier.verify_number(req.number)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
