from fastapi.testclient import TestClient
from app.main import app


def test_create_order():
    client = TestClient(app)
    payload = {
        "customerId": "cust_1",
        "items": [{"productId": "p1", "qty": 2, "unitPrice": 10.0}],
        "currency": "KES",
    }
    resp = client.post("/v1/orders", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["amount"] == 20.0
    assert data["status"] == "PENDING"