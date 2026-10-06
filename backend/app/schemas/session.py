from datetime import datetime
from pydantic import BaseModel


class SessionOut(BaseModel):
    id: int
    driver_id: int
    source: str
    start_time: datetime
    end_time: datetime | None
    duration_seconds: int
    average_safety_score: float
    minimum_safety_score: float
    drowsiness_events: int
    fatigue_events: int
    distraction_events: int
    phone_events: int
    critical_events: int

    model_config = {"from_attributes": True}
