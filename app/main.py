from typing import Union

from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/reflect")
async def reflect_json(request: Request):
    input_json = await request.json()
    return JSONResponse(content=input_json)