from fastapi import FastAPI
from app import encodeMsg, decodeMsg


app = FastAPI()


@app.get("/encode")
def encodeMessage(message:str):
    return {
        "data": encodeMsg.encodeData(message)
    }

@app.get("/decode")
def decodeMessage(message:str):
    return {
        "data":decodeMsg.decodeData(message)
    }