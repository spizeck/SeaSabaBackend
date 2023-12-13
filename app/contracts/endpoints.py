from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Session
from typing import List

from app.contracts import crud, schemas
from app.dependencies import get_db

router = APIRouter()

