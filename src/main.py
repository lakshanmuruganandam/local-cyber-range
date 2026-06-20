
from fastapi import FastAPI
from src.api.router import api_router

app = FastAPI(
    title="Autonomous Agent Core",
    description="Next-Generation Edge Inference Engine",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Engine is running flawlessly on edge."}
