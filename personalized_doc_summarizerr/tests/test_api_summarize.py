import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize_success():
    # Sample test PDF
    test_pdf_path = "app/pdf/sample_pdf.pdf"

    # Ensure sample file exists
    assert os.path.exists(test_pdf_path), "Missing sample PDF file."

    with open(test_pdf_path, "rb") as f:
        response = client.post(
            "/summarize",
            files={"file": ("sample_pdf.pdf", f, "application/pdf")},
            data={"persona": "Student"},
        )

    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 10


def test_invalid_persona():
    test_pdf_path = "app/pdf/sample.pdf"
    if not os.path.exists(test_pdf_path):
        return

    with open(test_pdf_path, "rb") as f:
        response = client.post(
            "/summarize",
            files={"file": ("sample.pdf", f, "application/pdf")},
            data={"persona": "Alien"},
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid persona selected."


def test_missing_file():
    response = client.post(
        "/summarize",
        data={"persona": "Student"},
    )
    assert response.status_code == 422  # Unprocessable Entity due to missing file
