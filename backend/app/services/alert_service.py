from datetime import datetime, timedelta, timezone


class AlertService:
    def __init__(self, cooldown_seconds: int = 8) -> None:
        self.cooldown = timedelta(seconds=cooldown_seconds)
        self.last_alert_at: dict[str, datetime] = {}

    def should_emit(self, key: str, now: datetime | None = None) -> bool:
        now = now or datetime.now(timezone.utc)
        previous = self.last_alert_at.get(key)
        if previous and now - previous < self.cooldown:
            return False
        self.last_alert_at[key] = now
        return True

    def evaluate(self, state: str, signals: dict, safety_score: int) -> list[dict]:
        candidates: list[tuple[str, int, str]] = []
        if state == "CRITICAL":
            candidates.append(("CRITICAL_RISK", 4, "Critical driver risk detected"))
        if signals.get("long_eye_closure"):
            candidates.append(("LONG_EYE_CLOSURE", 3, "Long eye closure detected"))
        if signals.get("yawning"):
            candidates.append(("YAWNING", 2, "Yawning detected"))
        if signals.get("gaze") in {"LEFT", "RIGHT", "DOWN"}:
            candidates.append(("LOOKING_AWAY", 2, "Driver looking away"))
        if signals.get("phone_risk", 0) > 50:
            candidates.append(("PHONE_DETECTED", 3, "Phone distraction risk detected"))
        if signals.get("lighting") in {"LOW_LIGHT", "NIGHT"}:
            candidates.append(("LOW_LIGHT", 1, "Low light condition detected"))

        alerts = []
        for key, severity, message in candidates:
            if self.should_emit(key):
                alerts.append({"type": key, "severity": severity, "message": message, "safety_score": safety_score})
        return alerts
