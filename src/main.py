from fastapi import FastAPI
from src.resource.authentication.api import auth_router


app = FastAPI()

app.include_router(auth_router)
