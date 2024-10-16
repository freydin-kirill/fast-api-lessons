from datetime import datetime
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)


# Fake BD
fake_users = [
    {"id": 1, "username": "Bob", "role": "admin"},
    {"id": 2, "username": "Claire", "role": "investor"},
    {"id": 3, "username": "Smith", "role": "trader"},
    {"id": 4, "username": "Homer", "role": "investor", "degree": [
        {"id": 1, "created_at": "2020-05-21T00:00:00", "type": "expert"}
    ]}
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: list[Degree] | None = []


@app.get("/users/{user_id}", response_model=list[User])
def get_user(user_id):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "USD", "amount": 2.15, "price": 123, "side": "sell"},
    {"id": 2, "user_id": 1, "currency": "USD", "amount": 2.15, "price": 125.6, "side": "buy"},
]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post("users/{user_id}")
def change_name(user_id: int, new_name: str):
    current_user = filter(lambda user: user.get("id") == user_id, fake_users)
    current_user["name"] = new_name
    return {"status": "success", "data": current_user}


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    amount: float
    price: float = Field(ge=0, example=123.45)
    side: str


@app.post("/trades")
def add_trade(trades: list[Trade]):
    fake_trades.extend(trades)
    return {"status": "success", "data": fake_trades}

