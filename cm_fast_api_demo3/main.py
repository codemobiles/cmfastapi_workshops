from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str

app = FastAPI()

@app.get("/login")
def login():
    return {"login": "get success"}


@app.post("/login")
def login():
    return {"login": "post success"}

@app.post("/register")
def register(user:User):
    return {"register": "post success", "detail":user}    


# https://www.youtube.com/watch?v=--LEfrXsx7g    