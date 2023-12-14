from fastapi import FastAPI
from app.users.endpoints import router as user_router

app = FastAPI()

app.include_router(user_router)