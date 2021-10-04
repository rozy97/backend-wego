from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.usecases import user

class User(BaseModel):
    name: str
    dob: str
    gender: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "TES BACKEND WEGODEV"}

@app.get("/users/{user_id}")
async def get_user_by_id(user_id):
    response = user.get_user_by_id(user_id)
    response_code = response['code']
    response_data = response['data']
    if response_code != 200:
        raise HTTPException(status_code=response_code, detail=response_data)
    
    return response_data

@app.post("/users/")
async def create_user(item: User):
    new_user = {
        'name': item.name,
        'dob': item.dob,
        'gender': item.gender
    }
    response = user.create_user(new_user)

    response_code = response['code']
    response_data = response['data']
    if response_code != 200:
        raise HTTPException(status_code=response_code, detail=response_data)
    
    return response_data
