from src.models import Vehicle
from src.database import session

async def list_vehicles():
    vehicles = session.query(Vehicle).filter_by(status="available").order_by(Vehicle.price).all()
    return [{"id": v.id, "brand": v.brand, "price": v.price} for v in vehicles]
