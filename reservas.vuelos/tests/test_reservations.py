import sys
import os
from fastapi.testclient import TestClient
from main import app

# Asegurar que el directorio raíz está en sys.path para que pueda importar `main.py`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)  

# PRUEBA 1: CREAR UNA RESERVA
def test_create_reservation():
    """
    Prueba la creación de una reserva.
    """
    response = client.post(
        "/",  
        json={
            "user_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "flight_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "seat_number": "12A"
        },
    )

    # Asegurar que la respuesta es exitosa antes de acceder al JSON
    assert response.status_code == 201, f"Error: {response.json()}"  

    data = response.json()
    print("Create Response:", data)  

    assert "id" in data  # La respuesta debe incluir el ID de la reserva
    assert data["flight_id"] == "69139a10-f38f-11ef-9cd2-0242ac120002"


# PRUEBA 2: OBTENER UNA RESERVA POR ID
def test_get_reservation():
    """
    Prueba la obtención de una reserva existente.
    """
    #Primero creamos una reserva antes de consultarla
    create_response = client.post(
        "/",  
        json={
            "user_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "flight_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "seat_number": "12A"
        },
    )

    assert create_response.status_code == 201, f"Error: {create_response.json()}"
    reservation_id = create_response.json()["id"]

    #Intentamos obtener la reserva creada
    response = client.get(f"/{reservation_id}")  
    assert response.status_code == 200, f"Error: {response.json()}"

    data = response.json()
    print("Get Response:", data)  

    assert data["id"] == reservation_id
    assert data["flight_id"] == "69139a10-f38f-11ef-9cd2-0242ac120002"

# PRUEBA 3: LISTAR TODAS LAS RESERVAS
def test_list_reservations():
    """
    Prueba la obtención de todas las reservas con paginación.
    """
    response = client.get("/")  
    assert response.status_code == 200, f"Error: {response.json()}"

    data = response.json()
    print("List Reservations Response:", data)  

    assert isinstance(data, dict)  # La respuesta debe ser un diccionario con paginación
    assert "items" in data  # Debe contener la lista de reservas
    assert isinstance(data["items"], list)  # Debe ser una lista

# PRUEBA 4: CANCELAR UNA RESERVA
def test_cancel_reservation():
    """
    Prueba la cancelación de una reserva existente sin eliminarla.
    """
    # Crear una reserva antes de cancelarla
    create_response = client.post(
        "/",
        json={
            "user_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "flight_id": "69139a10-f38f-11ef-9cd2-0242ac120002",
            "seat_number": "12A"
        },
    )

    assert create_response.status_code == 201, f"Error: {create_response.json()}"
    reservation_id = create_response.json()["id"]

    #Cancelar la reserva
    cancel_response = client.delete(f"/{reservation_id}")
    assert cancel_response.status_code == 204, f"Error: {cancel_response.json()}"

    #Obtener la reserva después de la cancelación
    get_response = client.get(f"/{reservation_id}")
    assert get_response.status_code == 200, f"Error: {get_response.json()}"

    data = get_response.json()
    print("Get After Cancel Response:", data)  

    assert data["id"] == reservation_id  #Solo verificar que la reserva sigue existiendo

