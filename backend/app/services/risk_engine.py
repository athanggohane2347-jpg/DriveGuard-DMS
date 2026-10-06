from dataclasses import dataclass


@dataclass
class RiskResult:
    safety_score: int
    risk_score: int
    contributors: list[dict]


class RiskEngine:
    def calculate(self, signals: dict) -> RiskResult:
        contributors: list[dict] = []

        def add(name: str, points: int, active: bool, detail: str) -> None:
            if active:
                contributors.append({"name": name, "points": -abs(points), "detail": detail})

        add("Face not detected", 35, not signals.get("face_present", True), "Driver face is not visible.")
        add("Camera blocked", 45, signals.get("camera_status") == "BLOCKED", "Camera feed may be covered or invalid.")
        add("Long eye closure", 25, signals.get("long_eye_closure", False), "Eyes closed beyond configured threshold.")
        add("Drowsiness", int(signals.get("drowsiness", 0) * 0.25), signals.get("drowsiness", 0) > 45, "Drowsiness score is elevated.")
        add("Fatigue", int(signals.get("fatigue", 0) * 0.18), signals.get("fatigue", 0) > 50, "Fatigue trend is elevated.")
        add("Yawning", 10, signals.get("yawning", False), "Mouth opening duration resembles yawning.")
        add("Head nodding", 15, signals.get("head_nodding", False), "Repeated downward head motion detected.")
        add("Looking away", 12, signals.get("gaze") in {"LEFT", "RIGHT", "DOWN"}, "Gaze/head direction is away from forward.")
        add("Phone distraction risk", 18, signals.get("phone_risk", 0) > 50, "Phone/object signal persisted with attention deviation.")
        add("Low light", 6, signals.get("lighting") in {"LOW_LIGHT", "NIGHT"}, "Low light can reduce confidence.")

        total_penalty = sum(abs(item["points"]) for item in contributors)
        safety_score = max(0, min(100, 100 - total_penalty))
        return RiskResult(safety_score=safety_score, risk_score=100 - safety_score, contributors=contributors)


def driver_state_from_signals(signals: dict, safety_score: int) -> str:
    if not signals.get("face_present", True):
        return "FACE_NOT_DETECTED"
    if safety_score <= 35 or signals.get("critical_eye_closure", False):
        return "CRITICAL"
    if signals.get("drowsiness", 0) > 65:
        return "DROWSY"
    if signals.get("fatigue", 0) > 60:
        return "FATIGUED"
    if signals.get("phone_risk", 0) > 50 or signals.get("gaze") in {"LEFT", "RIGHT", "DOWN"}:
        return "DISTRACTED"
    return "ATTENTIVE"
