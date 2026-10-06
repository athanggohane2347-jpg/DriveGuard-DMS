from collections import deque
from dataclasses import dataclass
from pathlib import Path
from time import time


@dataclass
class FrameRecord:
    timestamp: float
    frame: object


class CircularRecordingBuffer:
    def __init__(self, seconds: int = 10, fps: int = 15) -> None:
        self.frames: deque[FrameRecord] = deque(maxlen=seconds * fps)

    def add_frame(self, frame: object) -> None:
        self.frames.append(FrameRecord(time(), frame))

    def save_pre_event_manifest(self, output_dir: str, event_id: int) -> str:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        path = Path(output_dir) / f"event_{event_id}_prebuffer.txt"
        path.write_text(f"Buffered frames available: {len(self.frames)}\n", encoding="utf-8")
        return str(path)
