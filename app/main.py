
from fastapi import FastAPI
from app.routes import discovery, verification, simswap

app = FastAPI(title="IMC Open Gateway - Modular API Gateway")

app.include_router(discovery.router, prefix="/discover", tags=["discovery"])
app.include_router(verification.router, prefix="/verify-number", tags=["verification"])
app.include_router(simswap.router, prefix="/simswap", tags=["simswap"])

@app.get("/")
async def root():
    return {"project": "IMC Open Gateway - Modular API Gateway", "status": "ok"}
