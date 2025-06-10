from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_payment_methods_success():
    response = client.post("/payment/payment-methods", json={
        "product_id": "1",
        "price": 600,
        "currency": "USD",
        "category": "smartphones"
    })
    assert response.status_code == 200
    assert "credit" in response.json()

def test_post_payment_methods_failure():
    response = client.post("/payment/payment-methods", json={})
    assert response.status_code == 422