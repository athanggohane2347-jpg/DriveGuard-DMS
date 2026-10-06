import os
import psutil
from fastapi import APIRouter
from ..config import get_settings

router = APIRouter(prefix="/api/system", tags=["system"])


@router.get("/status")
def status() -> dict:
    settings = get_settings()
    return {
        "app": settings.app_name,
        "environment": settings.environment,
        "status": "ONLINE",
        "simulation_mode": settings.simulation_mode,
        "recording_enabled": settings.recording_enabled,
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "pid": os.getpid(),
        "model_path": settings.model_path,
        "camera": "SIMULATION" if settings.simulation_mode else f"CAMERA_{settings.camera_index}",
    }
