from dataclasses import dataclass


@dataclass
class ObjectDetection:
    label: str
    confidence: float
    bbox: tuple[int, int, int, int]


class ObjectDetector:
    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path
        self.available = bool(model_path)

    def detect(self, frame: object | None) -> list[ObjectDetection]:
        if frame is None or not self.available:
            return []
        return []
