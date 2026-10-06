from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"), index=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)
    event_type: Mapped[str] = mapped_column(String(80), index=True)
    severity: Mapped[int] = mapped_column(Integer, default=1)
    confidence: Mapped[float] = mapped_column(Float, default=0)
    safety_score: Mapped[float] = mapped_column(Float, default=100)
    description: Mapped[str] = mapped_column(String(500))
    snapshot_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    video_clip_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    session = relationship("DriverSession", back_populates="events")
