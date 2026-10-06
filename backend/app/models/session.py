from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class DriverSession(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.id"))
    source: Mapped[str] = mapped_column(String(40), default="SIMULATION")
    start_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[int] = mapped_column(Integer, default=0)
    average_safety_score: Mapped[float] = mapped_column(Float, default=100)
    minimum_safety_score: Mapped[float] = mapped_column(Float, default=100)
    drowsiness_events: Mapped[int] = mapped_column(Integer, default=0)
    fatigue_events: Mapped[int] = mapped_column(Integer, default=0)
    distraction_events: Mapped[int] = mapped_column(Integer, default=0)
    phone_events: Mapped[int] = mapped_column(Integer, default=0)
    critical_events: Mapped[int] = mapped_column(Integer, default=0)
    driver = relationship("Driver", back_populates="sessions")
    events = relationship("Event", back_populates="session", cascade="all, delete-orphan")
