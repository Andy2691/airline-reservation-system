from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_reservation():
    """
    Prueba la creación de una reserva.
    """
    response = client.post(
        "/reservations/",
        json={
            "user_id": "550e8400-e29b-41d4-a716-446655440000",
            "flight_code": "ABC123",
            "seat_number": "12A"
        },
    )
    assert response.status_code == 201  # Código HTTP esperado
    data = response.json()
    assert "id" in data  # La respuesta debe incluir el ID de la reserva
    assert data["flight_code"] == "ABC123"
