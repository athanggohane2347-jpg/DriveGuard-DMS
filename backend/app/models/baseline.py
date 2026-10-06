from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class DriverBaseline(Base):
    __tablename__ = "driver_baselines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.id"), unique=True)
    blink_rate: Mapped[float] = mapped_column(Float, default=15)
    eye_openness: Mapped[float] = mapped_column(Float, default=0.28)
    head_yaw: Mapped[float] = mapped_column(Float, default=0)
    head_pitch: Mapped[float] = mapped_column(Float, default=0)
    gaze_center: Mapped[float] = mapped_column(Float, default=0)
    calibrated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    driver = relationship("Driver", back_populates="baseline")
