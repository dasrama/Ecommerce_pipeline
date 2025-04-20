from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.config.config import initiate_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield
    print("Shutting down server")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
