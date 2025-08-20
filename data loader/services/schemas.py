from pydantic import BaseModel

class SoldierBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    rank: str

class SoldierCreate(SoldierBase):
    pass

class SoldierResponse(SoldierBase):
    id: str
