def classify_gaze(horizontal_ratio: float, vertical_ratio: float) -> str:
    if vertical_ratio > 0.68:
        return "DOWN"
    if horizontal_ratio < 0.38:
        return "LEFT"
    if horizontal_ratio > 0.62:
        return "RIGHT"
    return "FORWARD"
