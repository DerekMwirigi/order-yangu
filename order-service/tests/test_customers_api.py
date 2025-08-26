from fastapi.testclient import TestClient
from app.main import app


def test_create_customers():
    client = TestClient(app)
    payload = {
        "name": "Test Customer",
        "email": "test-customer@abc.xyz",
        "phone": "254706828000",
    }
    resp = client.post("/v1/customers", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["phone"] == "254706828000"