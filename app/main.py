from fastapi import FastAPI
from app.users.endpoints import router as user_router
from app.contracts.endpoints import router as contract_router

app = FastAPI()

app.include_router(user_router)
app.include_router(contract_router)
