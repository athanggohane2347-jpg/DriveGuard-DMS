from dataclasses import dataclass


@dataclass
class FaceDetection:
    present: bool
    confidence: float
    bbox: tuple[int, int, int, int] | None = None


class FaceDetector:
    def detect(self, frame: object | None) -> FaceDetection:
        if frame is None:
            return FaceDetection(False, 0)
        return FaceDetection(True, 0.75, (120, 80, 300, 300))
