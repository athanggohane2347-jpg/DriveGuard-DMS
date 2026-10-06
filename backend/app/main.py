from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import analytics, auth, dashboard, driver, events, sessions, settings, system
from .config import get_settings
from .database import init_db
from .websocket.driver_monitor import router as ws_router


settings_obj = get_settings()
app = FastAPI(
    title="DriveGuard DMS API",
    description="AI-powered driver monitoring research prototype API.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings_obj.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(driver.router)
app.include_router(sessions.router)
app.include_router(events.router)
app.include_router(analytics.router)
app.include_router(settings.router)
app.include_router(system.router)
app.include_router(ws_router)


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/")
def root() -> dict:
    return {"name": settings_obj.app_name, "status": "ONLINE", "docs": "/docs"}
