from fastapi.testclient import TestClient
from app.main import app


# test initiating a payment via stk push
def test_create_payment():
    client = TestClient(app)
    payload = {"orderId": "o1", "amount": 100.00, "msisdn": "254700000000"}
    resp = client.post("/v1/payments", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "INITIATED"