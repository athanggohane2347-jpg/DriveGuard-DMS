from collections.abc import Sequence
from .eye_analyzer import Point, distance


def mouth_aspect_ratio(points: Sequence[Point]) -> float:
    if len(points) != 8:
        raise ValueError("MAR requires 8 mouth landmark points")
    vertical_1 = distance(points[1], points[7])
    vertical_2 = distance(points[2], points[6])
    vertical_3 = distance(points[3], points[5])
    horizontal = distance(points[0], points[4])
    if horizontal == 0:
        return 0
    return (vertical_1 + vertical_2 + vertical_3) / (3.0 * horizontal)


def is_yawning(mar: float, threshold: float = 0.65) -> bool:
    return mar >= threshold
