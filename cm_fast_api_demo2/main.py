from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"root":"yes"}


@app.get("/courses")
def get_courses():
    return ["Angular", "Vuejs"]

@app.get("/course/{id}")
def get_course_by_id(id:int):
    return ["Angular", "Vuejs"][id]

# pydantic
@app.get("/auth/{action}/{token}")
def get_action_and_token(action:str, token:str, q1:Optional[str]=None):
    return {"action":action, "token":token, "q1": q1}