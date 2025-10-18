
import asyncio
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert "project" in res.json()

def test_discover():
    res = client.get("/discover/")
    assert res.status_code == 200
    data = res.json()
    assert "services" in data
