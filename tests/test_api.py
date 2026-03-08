# tests/test_api.py
from fastapi.testclient import TestClient
from api.predict_api import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fraud Detection API"}

def test_predict_endpoint():
    data = {"amount": 500, "country": 2, "device": 1}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "fraud" in response.json()
    assert response.json()["fraud"] in [0, 1]  # Model outputs either 0 or 1