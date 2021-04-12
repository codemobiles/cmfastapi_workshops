from fastapi import FastAPI

from fastapi.responses import FileResponse


some_file_path = "readme.txt"
app = FastAPI()


@app.get("/")
def main():
    return FileResponse(some_file_path)

@app.get("/download")
def download():
    return FileResponse(path="./readme.txt", media_type='text/plain',filename=some_file_path)

@app.get("/download/image")
def download():
    return FileResponse(path="./image.jpg", media_type='image/jpeg',filename="image.jpg")
