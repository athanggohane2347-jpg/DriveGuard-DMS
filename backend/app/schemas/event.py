from datetime import datetime
from pydantic import BaseModel


class EventOut(BaseModel):
    id: int
    session_id: int
    timestamp: datetime
    event_type: str
    severity: int
    confidence: float
    safety_score: float
    description: str
    snapshot_path: str | None = None
    video_clip_path: str | None = None

    model_config = {"from_attributes": True}
