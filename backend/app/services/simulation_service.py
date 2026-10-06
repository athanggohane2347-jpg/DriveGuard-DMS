import math
from datetime import datetime, timezone
from .alert_service import AlertService
from .fatigue_service import FatigueTrend
from .risk_engine import RiskEngine, driver_state_from_signals


class DriverSimulation:
    def __init__(self) -> None:
        self.tick = 0
        self.risk = RiskEngine()
        self.alerts = AlertService()
        self.fatigue = FatigueTrend()

    def next_payload(self, session_id: int | None = None) -> dict:
        self.tick += 1
        wave = (math.sin(self.tick / 8) + 1) / 2
        fatigue_score = min(92, 12 + self.tick * 0.18 + wave * 18)
        drowsiness = min(95, 10 + wave * 35 + (18 if self.tick % 47 in range(38, 47) else 0))
        distraction = 8 + (45 if self.tick % 31 in range(22, 29) else 0)
        phone_risk = 70 if self.tick % 59 in range(45, 54) else 0
        face_present = self.tick % 83 not in range(73, 80)
        long_eye = self.tick % 47 in range(42, 47)
        gaze = "RIGHT" if distraction > 40 else "FORWARD"
        lighting = "LOW_LIGHT" if self.tick % 101 > 88 else "DAY"
        trend = self.fatigue.add(fatigue_score)
        signals = {
            "face_present": face_present,
            "camera_status": "SIMULATION",
            "long_eye_closure": long_eye,
            "critical_eye_closure": long_eye and drowsiness > 60,
            "drowsiness": drowsiness,
            "fatigue": fatigue_score,
            "yawning": self.tick % 37 in range(30, 34),
            "head_nodding": self.tick % 67 in range(60, 64),
            "gaze": gaze,
            "phone_risk": phone_risk,
            "lighting": lighting,
        }
        risk = self.risk.calculate(signals)
        state = driver_state_from_signals(signals, risk.safety_score)
        alerts = self.alerts.evaluate(state, signals, risk.safety_score)
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "session_id": session_id,
            "mode": "SIMULATION MODE",
            "driver_state": state,
            "safety_score": risk.safety_score,
            "risk_score": risk.risk_score,
            "contributors": risk.contributors,
            "scores": {
                "drowsiness": round(drowsiness, 1),
                "fatigue": round(fatigue_score, 1),
                "distraction": round(distraction, 1),
                "attention": max(0, round(100 - distraction, 1)),
                "phone_risk": phone_risk,
            },
            "detections": {
                "eyes": "CLOSED" if long_eye else "OPEN",
                "blinking": "LONG_BLINK" if long_eye else "NORMAL",
                "yawning": signals["yawning"],
                "head_pose": "NODDING" if signals["head_nodding"] else "NORMAL",
                "gaze": gaze,
                "phone": "DETECTED" if phone_risk > 0 else "NOT_DETECTED",
                "face": "DETECTED" if face_present else "FACE_NOT_DETECTED",
            },
            "metrics": {
                "fps": 30,
                "latency_ms": 14 + round(wave * 7, 1),
                "blink_rate": 14 + round(wave * 8, 1),
                "yawns_this_session": self.tick // 37,
                "fatigue_trend": trend,
                "cpu": 22 + round(wave * 16, 1),
                "gpu": None,
            },
            "head_pose": {"yaw": round(wave * 8 - 4, 1), "pitch": round(wave * 5 - 2, 1), "roll": round(wave * 3 - 1, 1)},
            "camera": {"status": "SIMULATION", "lighting": lighting},
            "alerts": alerts,
            "notice": "Simulation values are demo data, not real AI detections.",
        }
