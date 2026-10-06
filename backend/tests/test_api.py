from fastapi.testclient import TestClient
from app.database import init_db
from app.main import app


init_db()
client = TestClient(app)


def auth_headers():
    payload = {"email": "test@example.com", "password": "DriveGuard123!", "name": "Test Driver"}
    response = client.post("/api/auth/register", json=payload)
    if response.status_code == 409:
        response = client.post("/api/auth/login", json={"email": payload["email"], "password": payload["password"]})
    assert response.status_code == 200
    return {"Authorization": f"Bearer {response.json()['access_token']}"}


def test_status_endpoint():
    response = client.get("/api/system/status")
    assert response.status_code == 200
    assert response.json()["status"] == "ONLINE"


def test_session_lifecycle():
    headers = auth_headers()
    started = client.post("/api/session/start", headers=headers)
    assert started.status_code == 200
    session_id = started.json()["id"]
    stopped = client.post(f"/api/session/stop?session_id={session_id}", headers=headers)
    assert stopped.status_code == 200
    assert stopped.json()["id"] == session_id


def test_dashboard_requires_auth():
    assert client.get("/api/dashboard").status_code == 401
