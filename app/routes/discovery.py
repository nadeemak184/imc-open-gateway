
from fastapi import APIRouter
from pydantic import BaseModel
from app.modules import discovery as discovery_module

router = APIRouter()

class DiscoveryResponse(BaseModel):
    services: dict

@router.get("/", response_model=DiscoveryResponse)
async def discover():
    # discovery logic is delegated to a pluggable module
    services = await discovery_module.find_services()
    return {"services": services}
