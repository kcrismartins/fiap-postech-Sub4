from fastapi import FastAPI, HTTPException
from src.database import init_db
from src.services.listing import list_vehicles
from src.services.sales import register_sale

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/vehicles")
async def get_vehicles():
    return await list_vehicles()

@app.post("/sales")
async def post_sale(sale_data: dict):
    try:
        return await register_sale(sale_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
