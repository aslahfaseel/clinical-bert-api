import sys
import os
from fastapi.testclient import TestClient
from app.main import app

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

client = TestClient(app)

test_cases = [
    ("The patient denies chest pain.", "ABSENT"),
    ("He has a history of hypertension.", "PRESENT"),
    (
        "If the patient experiences dizziness, "
        "reduce the dosage.",
        "CONDITIONAL",
    ),
    ("No signs of pneumonia were observed.", "ABSENT"),
]


def test_predictions():
    response = client.post(
        "/predict",
        json={"sentence": "The patient denies chest pain."}
    )

    expected_label = "ABSENT"
    assert response.status_code == 200
    assert response.json()["label"] == expected_label
