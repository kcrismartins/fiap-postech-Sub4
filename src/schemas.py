from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleSchema(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str
    price: float
    status: str

    class Config:
        orm_mode = True  # Para suportar objetos do SQLAlchemy

class SaleSchema(BaseModel):
    id: int
    vehicle_id: int
    buyer_cpf: str
    sale_date: datetime

    class Config:
        orm_mode = True
