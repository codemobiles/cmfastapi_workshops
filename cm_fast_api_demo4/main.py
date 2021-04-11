from typing import Optional
from fastapi import FastAPI, Form

app = FastAPI()

# curl tutorial
# https://www.youtube.com/watch?v=--LEfrXsx7g


@app.post("/register")
def post_register(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}    