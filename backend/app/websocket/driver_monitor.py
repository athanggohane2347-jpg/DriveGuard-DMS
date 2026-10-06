import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models.event import Event
from ..services.simulation_service import DriverSimulation

router = APIRouter()


@router.websocket("/ws/driver-monitor")
async def driver_monitor(websocket: WebSocket) -> None:
    await websocket.accept()
    simulation = DriverSimulation()
    db: Session = SessionLocal()
    session_id: int | None = None
    try:
        while True:
            payload = simulation.next_payload(session_id=session_id)
            for alert in payload["alerts"]:
                if session_id:
                    db.add(
                        Event(
                            session_id=session_id,
                            event_type=alert["type"],
                            severity=alert["severity"],
                            confidence=0.82,
                            safety_score=payload["safety_score"],
                            description=alert["message"],
                        )
                    )
                    db.commit()
            await websocket.send_json(payload)
            try:
                message = await asyncio.wait_for(websocket.receive_json(), timeout=1.0)
                if message.get("type") == "SET_SESSION":
                    session_id = message.get("session_id")
            except asyncio.TimeoutError:
                continue
    except WebSocketDisconnect:
        pass
    finally:
        db.close()
