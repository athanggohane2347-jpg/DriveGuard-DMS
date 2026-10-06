from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.driver import Driver
from ..models.event import Event
from ..models.session import DriverSession
from ..models.user import User
from ..schemas.session import SessionOut

router = APIRouter(prefix="/api", tags=["sessions"])


def _driver(db: Session, user: User) -> Driver:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver profile not found")
    return driver


@router.get("/sessions", response_model=list[SessionOut])
def list_sessions(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> list[DriverSession]:
    driver = _driver(db, user)
    return db.query(DriverSession).filter(DriverSession.driver_id == driver.id).order_by(DriverSession.start_time.desc()).all()


@router.get("/sessions/{session_id}", response_model=SessionOut)
def get_session(session_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> DriverSession:
    driver = _driver(db, user)
    session = db.query(DriverSession).filter(DriverSession.id == session_id, DriverSession.driver_id == driver.id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@router.post("/session/start", response_model=SessionOut)
def start_session(source: str = "SIMULATION", db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> DriverSession:
    driver = _driver(db, user)
    session = DriverSession(driver_id=driver.id, source=source)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@router.post("/session/stop", response_model=SessionOut)
def stop_session(session_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> DriverSession:
    driver = _driver(db, user)
    session = db.query(DriverSession).filter(DriverSession.id == session_id, DriverSession.driver_id == driver.id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.end_time = datetime.now(timezone.utc).replace(tzinfo=None)
    session.duration_seconds = max(0, int((session.end_time - session.start_time).total_seconds()))
    events = db.query(Event).filter(Event.session_id == session.id).all()
    if events:
        session.minimum_safety_score = min(event.safety_score for event in events)
        session.average_safety_score = sum(event.safety_score for event in events) / len(events)
        session.drowsiness_events = sum(1 for event in events if event.event_type in {"DROWSINESS", "LONG_EYE_CLOSURE"})
        session.fatigue_events = sum(1 for event in events if event.event_type in {"YAWNING", "HEAD_NODDING"})
        session.distraction_events = sum(1 for event in events if event.event_type in {"DISTRACTION", "LOOKING_AWAY"})
        session.phone_events = sum(1 for event in events if event.event_type == "PHONE_DETECTED")
        session.critical_events = sum(1 for event in events if event.severity >= 4)
    db.commit()
    db.refresh(session)
    return session
