import math
from collections.abc import Sequence

Point = tuple[float, float]


def distance(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def eye_aspect_ratio(points: Sequence[Point]) -> float:
    if len(points) != 6:
        raise ValueError("EAR requires 6 eye landmark points")
    vertical_1 = distance(points[1], points[5])
    vertical_2 = distance(points[2], points[4])
    horizontal = distance(points[0], points[3])
    if horizontal == 0:
        return 0
    return (vertical_1 + vertical_2) / (2.0 * horizontal)


def classify_eye_state(ear: float, threshold: float = 0.21) -> str:
    if ear <= threshold * 0.72:
        return "CLOSED"
    if ear <= threshold:
        return "PARTIALLY_CLOSED"
    return "OPEN"
