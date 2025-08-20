from fastapi import FastAPI
from schemas import SoldierCreate, SoldierResponse
from DAL import create_soldier as cs, get_soldier as gs, update_soldier as us, delete_soldier as ds

app = FastAPI()

@app.post("/soldiers/", response_model=SoldierResponse)
def create_soldier(soldier: SoldierCreate):
    s = cs(soldier.model_dump())
    return SoldierResponse(**s.__dict__)

@app.get("/soldiers/{soldier_id}", response_model=SoldierResponse)
def read_soldier(soldier_id: str):
    s = gs(soldier_id)
    return SoldierResponse(**s.__dict__)

@app.put("/soldiers/{soldier_id}", response_model=SoldierResponse)
def update_soldier(soldier_id: str, soldier: SoldierCreate):
    s = us(soldier_id, soldier.model_dump())
    return SoldierResponse(**s.__dict__)

@app.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id: str):
    ds(soldier_id)
    return {"message": "Soldier deleted successfully"}


