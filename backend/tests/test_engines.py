from datetime import datetime, timedelta, timezone
from app.services.alert_service import AlertService
from app.services.risk_engine import RiskEngine, driver_state_from_signals


def test_risk_score_explainable():
    result = RiskEngine().calculate(
        {
            "face_present": True,
            "long_eye_closure": True,
            "drowsiness": 70,
            "fatigue": 20,
            "yawning": False,
            "head_nodding": False,
            "gaze": "FORWARD",
            "phone_risk": 0,
            "lighting": "DAY",
        }
    )
    assert result.safety_score < 75
    assert any(item["name"] == "Long eye closure" for item in result.contributors)


def test_driver_state_critical():
    assert driver_state_from_signals({"face_present": True, "critical_eye_closure": True}, 40) == "CRITICAL"


def test_alert_cooldown():
    service = AlertService(cooldown_seconds=10)
    now = datetime.now(timezone.utc)
    assert service.should_emit("LOOKING_AWAY", now)
    assert not service.should_emit("LOOKING_AWAY", now + timedelta(seconds=2))
    assert service.should_emit("LOOKING_AWAY", now + timedelta(seconds=11))
