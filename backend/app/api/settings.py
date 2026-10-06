from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.security import get_current_user
from ..database import get_db
from ..models.user import User
from ..schemas.settings import SettingsOut, SettingsUpdate
from ..services.settings_service import get_settings_map, update_settings_map

router = APIRouter(prefix="/api/settings", tags=["settings"])


@router.get("", response_model=SettingsOut)
def get_settings(db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> dict:
    return get_settings_map(db)


@router.put("", response_model=SettingsOut)
def put_settings(payload: SettingsUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> dict:
    return update_settings_map(db, payload.model_dump())
