from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>CodeMobiles</title>
        </head>
        <body>
            <h1>FastAPI</h1>
        </body>
    </html>
    """

@app.get("/legacy/")
async def read_items():
   data = """<?xml version="1.0"?>
     <shampoo>
     <Header>
        Apply shampoo here.
      </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """ 
   return Response(content=data, media_type="application/xml")


@app.get("/typer")
async def read_typer():
    return RedirectResponse("https://typer.tiangolo.com")