from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from app.dependencies import get_db

router = APIRouter()