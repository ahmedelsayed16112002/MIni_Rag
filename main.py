from fastapi import FastAPI
from base import base
from  dotenv  import load_dotenv
load_dotenv()

app = FastAPI()

app.include_router(base)     

