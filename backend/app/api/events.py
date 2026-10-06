from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.driver import Driver
from ..models.event import Event
from ..models.session import DriverSession
from ..models.user import User
from ..schemas.event import EventOut

router = APIRouter(prefix="/api/events", tags=["events"])


@router.get("", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> list[Event]:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    return (
        db.query(Event)
        .join(DriverSession)
        .filter(DriverSession.driver_id == driver.id)
        .order_by(Event.timestamp.desc())
        .limit(200)
        .all()
    )


@router.get("/{event_id}", response_model=EventOut)
def get_event(event_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> Event:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    event = db.query(Event).join(DriverSession).filter(Event.id == event_id, DriverSession.driver_id == driver.id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
