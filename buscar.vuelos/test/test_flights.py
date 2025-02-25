import random
from typing import Dict

from fastapi.testclient import TestClient

from app.database.conn import Base, engine
from main import app

client = TestClient(app)

Base.metadata.create_all(bind=engine)

def test_search() -> None:

    response = client.get(
        "/",
        params={
            
        },
    )

    data = response.json()
    vuelos = data["items"]
    assert vuelos[0]["id"] is not None
    