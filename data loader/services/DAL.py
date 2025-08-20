from pymongo import MongoClient
from bson import ObjectId
from fastapi import HTTPException
from soldier import Soldier

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client["enemy_soldiers"]
collection = db["soldier_details"]


def create_soldier(data: dict) -> Soldier:
    result = collection.insert_one(data)
    return Soldier(
        id=str(result.inserted_id),
        first_name=data["first_name"],
        last_name=data["last_name"],
        phone=data["phone"],
        rank=data["rank"]
    )


def get_soldier(soldier_id: str) -> Soldier:
    soldier = collection.find_one({"_id": ObjectId(soldier_id)})
    if not soldier:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return Soldier(
        id=str(soldier["_id"]),
        first_name=soldier["first_name"],
        last_name=soldier["last_name"],
        phone=soldier["phone"],
        rank=soldier["rank"]
    )


def update_soldier(soldier_id: str, data: dict) -> Soldier:
    updated = collection.find_one_and_update(
        {"_id": ObjectId(soldier_id)},
        {"$set": data},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return Soldier(
        id=str(updated["_id"]),
        first_name=updated["first_name"],
        last_name=updated["last_name"],
        phone=updated["phone"],
        rank=updated["rank"]
    )


def delete_soldier(soldier_id: str) -> bool:
    result = collection.delete_one({"_id": ObjectId(soldier_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return True


