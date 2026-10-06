from pydantic import BaseModel


class SettingsOut(BaseModel):
    ear_threshold: float
    eye_closure_warning_ms: int
    eye_closure_critical_ms: int
    yawn_threshold: float
    looking_away_warning_ms: int
    looking_away_high_ms: int
    alert_cooldown_seconds: int
    fatigue_sensitivity: float
    phone_detection_confidence: float
    recording_enabled: bool
    night_mode: str
    camera_selection: str
    processing_resolution: str
    demo_mode: bool


class SettingsUpdate(SettingsOut):
    pass
