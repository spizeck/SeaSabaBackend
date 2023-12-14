from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get('/hotels', response_model=List[schemas.Hotel])
async def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_hotels(db, skip=skip, limit=limit)


@router.get('/hotels/{hotel_id}', response_model=schemas.Hotel)
async def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    if not crud.get_hotel(db, id=hotel_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found"
        )
    return crud.get_hotel(db, id=hotel_id)
