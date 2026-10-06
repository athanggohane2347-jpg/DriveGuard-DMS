from collections import Counter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.driver import Driver
from ..models.event import Event
from ..models.session import DriverSession
from ..models.user import User

router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("")
def analytics(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> dict:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    sessions = db.query(DriverSession).filter(DriverSession.driver_id == driver.id).all()
    events = db.query(Event).join(DriverSession).filter(DriverSession.driver_id == driver.id).all()
    by_type = Counter(event.event_type for event in events)
    by_severity = Counter(str(event.severity) for event in events)
    score_series = [{"time": s.start_time.isoformat(), "score": round(s.average_safety_score, 1)} for s in sessions]
    fatigue_series = [{"time": event.timestamp.isoformat(), "fatigue": max(0, 100 - event.safety_score)} for event in events[-50:]]
    return {
        "totals": {
            "sessions": len(sessions),
            "driving_time_seconds": sum(s.duration_seconds for s in sessions),
            "average_safety_score": round(sum(s.average_safety_score for s in sessions) / len(sessions), 1) if sessions else 100,
            "warnings": sum(1 for event in events if event.severity >= 2),
            "critical_events": sum(1 for event in events if event.severity >= 4),
        },
        "events_by_type": dict(by_type),
        "events_by_severity": dict(by_severity),
        "safety_score_over_time": score_series,
        "fatigue_over_time": fatigue_series,
        "drowsiness_over_time": fatigue_series,
        "distraction_over_time": fatigue_series,
        "blink_frequency": [{"time": "now", "value": 16}],
        "yawning_frequency": [{"time": "now", "value": by_type.get("YAWNING", 0)}],
    }
