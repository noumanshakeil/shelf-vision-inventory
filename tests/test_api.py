from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["service"] == "shelf-vision-inventory"


def test_list_and_action():
    r = client.get("/api/shelves")
    assert r.status_code == 200
    assert "shelves" in r.json()

    r2 = client.post("/api/count_stock", json={"prompt": "smoke test"})
    assert r2.status_code == 200
    body = r2.json()
    assert body["ok"] is True
    assert "result" in body
