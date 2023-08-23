from fastapi import FastAPI
from beanie import init_beanie
import motor.motor_asyncio

from models.user import *

app = FastAPI()










@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )
    await init_beanie(database=client.autentification_service, document_models=[User])