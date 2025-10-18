
# IMC Open Gateway - Modular API Gateway (Hackathon Entry)

**Location:** IMC Open Gateway Hackathon — Yashobhoomi Convention Centre, New Delhi  
**Project:** Modular API gateway tool to simplify developer interactions with telecom network services (Open Gateway APIs)  
**Languages:** Python (FastAPI) + JavaScript (Node CLI)  
**Role:** Backend development & API integration

## What this repository contains

- `backend/` — FastAPI service that exposes modular endpoints:
  - `/discover` — automated service discovery (mocked / pluggable)
  - `/verify-number` — number verification workflow (example)
  - `/simswap` — SIM-swap detection scaffold
- `cli/` — Node.js CLI tool to interact with the backend easily
- `scripts/` — helper scripts for local testing and bootstrapping
- `Dockerfile`, `docker-compose.yml` — run the backend locally in Docker
- `.github/workflows/ci.yml` — simple CI that installs dependencies and runs linters/tests
- `examples/` — example integration snippets for Python & JS
- `LICENSE` — MIT

## Quickstart (local)

Requirements:
- Python 3.10+
- Node.js 18+
- (optional) Docker

1. Start backend:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Install CLI:
```bash
cd cli
npm install
node index.js --help
```

3. Try an endpoint:
```bash
# From project root
node cli/index.js discover --base http://localhost:8000
node cli/index.js verify-number --base http://localhost:8000 --number +911234567890
```

## Notes
- Network provider integrations are _mocked_ and meant to be replaced with real Open Gateway API calls.
- The backend is designed to be modular — add providers in `app/modules/providers/` and register them in `app/core/config.py`.

