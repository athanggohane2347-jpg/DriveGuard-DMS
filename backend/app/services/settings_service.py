from sqlalchemy.orm import Session
from ..models.setting import Setting


DEFAULT_SETTINGS: dict[str, object] = {
    "ear_threshold": 0.21,
    "eye_closure_warning_ms": 900,
    "eye_closure_critical_ms": 1800,
    "yawn_threshold": 0.65,
    "looking_away_warning_ms": 1000,
    "looking_away_high_ms": 3000,
    "alert_cooldown_seconds": 8,
    "fatigue_sensitivity": 1.0,
    "phone_detection_confidence": 0.45,
    "recording_enabled": False,
    "night_mode": "AUTO",
    "camera_selection": "SIMULATION",
    "processing_resolution": "640x480",
    "demo_mode": True,
}


def _parse(value: str, default: object) -> object:
    if isinstance(default, bool):
        return value.lower() == "true"
    if isinstance(default, int):
        return int(value)
    if isinstance(default, float):
        return float(value)
    return value


def get_settings_map(db: Session) -> dict[str, object]:
    rows = {row.key: row.value for row in db.query(Setting).all()}
    return {key: _parse(rows.get(key, str(default)), default) for key, default in DEFAULT_SETTINGS.items()}


def update_settings_map(db: Session, payload: dict[str, object]) -> dict[str, object]:
    for key, value in payload.items():
        if key not in DEFAULT_SETTINGS:
            continue
        row = db.query(Setting).filter(Setting.key == key).first()
        if row:
            row.value = str(value)
        else:
            db.add(Setting(key=key, value=str(value)))
    db.commit()
    return get_settings_map(db)
