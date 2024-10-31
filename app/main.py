from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies import dep_token, dep_form_data, dep_current_active_user
from app.database import fake_users_db
from app.models import UserInDB

app = FastAPI()

origins = [
    'http://localhost:4321/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def fake_hash_password(password: str):
    return "fakehashed" + password

@app.get("/users/me")
async def read_users_me(current_user: dep_current_active_user):
    return current_user

@app.get("/items/")
async def read_items(token: dep_token):
    return {"token": token}

@app.post("/token")
async def login(form_data: dep_form_data):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInDB(**user_dict)

    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

