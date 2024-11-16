import pytest
from httpx import AsyncClient
from src.main import app
from src.database import session
from src.models import Vehicle, Sale

@pytest.fixture(scope="module")
def test_client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    session.query(Sale).delete()
    session.query(Vehicle).delete()
    session.commit()
    session.add(Vehicle(id=1, brand="Toyota", model="Corolla", year=2020, color="Black", price=20000, status="available"))
    session.commit()

async def test_register_sale(test_client):
    sale_data = {"vehicle_id": 1, "buyer_cpf": "12345678901", "sale_date": "2024-11-15"}
    response = await test_client.post("/sales", json=sale_data)
    assert response.status_code == 200

    # Verifica no banco de dados
    sale = session.query(Sale).filter_by(vehicle_id=1).first()
    assert sale is not None
    assert sale.buyer_cpf == "12345678901"
    vehicle = session.query(Vehicle).filter_by(id=1).first()
    assert vehicle.status == "sold"
