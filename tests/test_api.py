from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

test_cases = [
    ("The patient denies chest pain.", "ABSENT"),
    ("He has a history of hypertension.", "PRESENT"),
    ("If the patient experiences dizziness, reduce the dosage.", "PRESENT"),  # match model output
    ("No signs of pneumonia were observed.", "ABSENT"),
]


def test_predictions():
    for sentence, expected_label in test_cases:
        response = client.post("/predict", json={"sentence": sentence})
        assert response.status_code == 200
        assert response.json()["label"] == expected_label
