from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
load_dotenv()
from models import Alert


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def main():
    return {"message": "Pong!"}

@app.post("/alert/receive")
def receive_alert(alert: Alert):
    print(alert)
    if alert.side == "BUY":
        print("BUY")
    elif alert.side == "SELL":
        print("SELL")
        
    return {"message": "Order Created"}