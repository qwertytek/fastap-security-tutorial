from fastapi import FastAPI
from app.dependencies import dep_current_user, dep_token
from app.database import fake_users_db

app = FastAPI()

@app.get("/users/me")
async def read_users_me(current_user: dep_current_user):
    return current_user

@app.get("/items/")
async def read_items(token: dep_token):
    return {"token": token}