from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/share", StaticFiles(directory="share"), name="share")
app.mount("/root", StaticFiles(directory="./"), name="root")