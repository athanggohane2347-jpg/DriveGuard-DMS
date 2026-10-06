from dataclasses import dataclass


@dataclass
class CameraStatus:
    status: str
    lighting: str
    fps: float
    latency_ms: float
    message: str = ""


class CameraService:
    def __init__(self, source: str = "SIMULATION") -> None:
        self.source = source

    def status(self) -> CameraStatus:
        if self.source == "SIMULATION":
            return CameraStatus("SIMULATION", "DAY", 30.0, 12.0, "SIMULATION MODE")
        return CameraStatus("CONNECTED", "DAY", 24.0, 22.0)
