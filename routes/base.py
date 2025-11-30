from fastapi import APIRouter
import os 



base = APIRouter(
    prefix="/API/NLP",
    tags=["API/NLP"],
)  

@base.get('/')
async def welcome():
    App_name = os.getenv("APP_NAME")
    App_version = os.getenv("APP_VERSION")
    return {"App_name": App_name, "App_version": App_version}