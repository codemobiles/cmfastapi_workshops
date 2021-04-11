from typing import Optional
from fastapi import FastAPI, Form
from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str


app = FastAPI()

@app.post("/login")
def post_login(user:User):
    return {"login": user}    

@app.post("/register")
def post_register(username: str = Form(...), password: str = Form(...)):
    return {"u": username, "p": password} 

@app.delete("/user/{id}")
def delete_user(id:int, user:User):
    return {"delete": id, "user": user}           

@app.put("/user/{id}")
def update_user(id:int, user:User):
    return {"update": id, "user": user}               