from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    price = Column(Float)
    status = Column(String, default="available")  # available or sold

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer)
    buyer_cpf = Column(String)
    sale_date = Column(DateTime)
