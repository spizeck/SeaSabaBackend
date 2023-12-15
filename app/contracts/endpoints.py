from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get('/hotels', response_model=List[schemas.Hotel], tags=['Group Contract Operations'])
async def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_hotels(db, skip=skip, limit=limit)


@router.get('/hotels/{hotel_id}', response_model=schemas.Hotel, tags=['Group Contract Operations'])
async def read_hotel(hotel_id: int, db: Session = Depends(get_db)):
    if not crud.get_hotel(db, hotel_id=hotel_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found"
        )
    return crud.get_hotel(db, hotel_id=hotel_id)


@router.post('/hotels', response_model=schemas.Hotel, tags=['Group Contract Operations'])
async def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db)):
    if crud.get_hotel_by_name(db, name=hotel.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Hotel name already exists"
        )
    return crud.create_hotel(db, hotel=hotel)


@router.put('/hotels/{hotel_id}', response_model=schemas.Hotel, tags=['Group Contract Operations'])
async def update_hotel(hotel_id: int, hotel: schemas.HotelUpdate, db: Session = Depends(get_db)):
    db_hotel = crud.get_hotel(db, hotel_id=hotel_id)
    if not db_hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found"
        )
    return crud.update_hotel(db, hotel_id=hotel_id, hotel_data=hotel)
