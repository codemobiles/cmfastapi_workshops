from typing import Optional
from fastapi import FastAPI, Form, Body
from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str


app = FastAPI()


@app.post("/register")
def post_register(user:User, level:str = Body(...)):
    return {**user.dict(), "level": level} 
