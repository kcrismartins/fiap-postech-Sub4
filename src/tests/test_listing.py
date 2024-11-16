import pytest
from httpx import AsyncClient
from src.main import app
from src.database import session
from src.models import Vehicle

@pytest.fixture(scope="module")
def test_client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # Limpa e preenche o banco de dados para cada teste
    session.query(Vehicle).delete()
    session.commit()
    session.add_all([
        Vehicle(brand="Toyota", model="Corolla", year=2020, color="Black", price=20000),
        Vehicle(brand="Honda", model="Civic", year=2019, color="White", price=18000),
    ])
    session.commit()

async def test_list_vehicles(test_client):
    response = await test_client.get("/vehicles")
    assert response.status_code == 200
    vehicles = response.json()
    assert len(vehicles) == 2
    assert vehicles[0]["brand"] == "Honda"  # Mais barato primeiro
    assert vehicles[1]["brand"] == "Toyota"
