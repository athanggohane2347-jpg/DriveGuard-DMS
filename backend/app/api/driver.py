from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.driver import Driver
from ..models.user import User

router = APIRouter(prefix="/api/driver", tags=["driver"])


@router.get("")
def get_driver(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> dict:
    driver = db.query(Driver).filter(Driver.user_id == user.id).first()
    total_sessions = len(driver.sessions) if driver else 0
    total_events = sum(len(session.events) for session in driver.sessions) if driver else 0
    avg = sum(s.average_safety_score for s in driver.sessions) / total_sessions if total_sessions else 100
    return {
        "id": driver.id,
        "name": driver.name,
        "profile_image": driver.profile_image,
        "calibration_status": "CALIBRATED" if driver.baseline else "NOT_CALIBRATED",
        "average_safety_score": round(avg, 1),
        "total_sessions": total_sessions,
        "total_events": total_events,
    }
