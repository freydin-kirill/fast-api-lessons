from fastapi import FastAPI
from sqlalchemy.testing.pickleable import User

app = FastAPI(
    title="Trading App"
)


# Fake BD
fake_users = [
    {"id": 1, "username": "Bob", "role": "admin"},
    {"id": 2, "username": "Claire", "role": "investor"},
    {"id": 3, "username": "Smith", "role": "trader"}
]


@app.get("/users/{user_id}")
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
