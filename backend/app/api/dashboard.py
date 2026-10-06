from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.driver import Driver
from ..models.event import Event
from ..models.session import DriverSession
from ..models.user import User

router = APIRouter(prefix="/api", tags=["dashboard"])


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> dict:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    sessions = db.query(DriverSession).filter(DriverSession.driver_id == driver.id).all() if driver else []
    events_query = db.query(Event).join(DriverSession).filter(DriverSession.driver_id == driver.id) if driver else db.query(Event).filter(False)
    events = events_query.order_by(Event.timestamp.desc()).limit(8).all()
    avg_score = db.query(func.avg(DriverSession.average_safety_score)).filter(DriverSession.driver_id == driver.id).scalar() if driver else 100
    return {
        "system_status": "ONLINE",
        "camera_status": "SIMULATION",
        "current_session": sessions[-1].id if sessions else None,
        "driver_state": "ATTENTIVE",
        "safety_score": round(avg_score or 100, 1),
        "totals": {
            "sessions": len(sessions),
            "events": events_query.count(),
            "critical_events": events_query.filter(Event.severity >= 4).count(),
        },
        "recent_events": [
            {
                "id": event.id,
                "timestamp": event.timestamp.isoformat(),
                "type": event.event_type,
                "severity": event.severity,
                "description": event.description,
            }
            for event in events
        ],
    }
