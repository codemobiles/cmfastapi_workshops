


from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World", "MyName": "Lek CodeMobiles"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = "none"):
    return {"item_id": item_id, "q": q}

# http://localhost:8000/courses/1/bangkok?q=lek
@app.get("/courses/{course_id}/{place}")
def get_courses(course_id: int, place: str,  q: Optional[str] = None, price: Optional[int] = 0):
    return {"course_id": course_id, "q": q, "price":price, "place": place}
