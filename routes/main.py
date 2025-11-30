from fastapi import FastAPI
from routes.base import base   
from  dotenv  import load_dotenv
load_dotenv()

app = FastAPI()

app.include_router(base)     

