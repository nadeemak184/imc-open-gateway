
from fastapi import APIRouter
from pydantic import BaseModel
from app.modules import simswap as sim_module

router = APIRouter()

class SimSwapCheckRequest(BaseModel):
    number: str

class SimSwapCheckResponse(BaseModel):
    number: str
    risk_score: float
    reason: str = ""

@router.post("/", response_model=SimSwapCheckResponse)
async def check(req: SimSwapCheckRequest):
    res = await sim_module.check_simswap(req.number)
    return res
