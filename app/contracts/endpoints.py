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


@router.get('/hotels/{hotel_id}/booking_policies', response_model=List[schemas.BookingPolicy],
            tags=['Group Contract Operations'])
async def get_booking_policies(hotel_id: int, db: Session = Depends(get_db)):
    policies = crud.get_booking_policies(db, hotel_id=hotel_id)
    if not policies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking policies not found"
        )
    return policies


@router.get('/hotels/booking_policy/{id}', response_model=schemas.BookingPolicy, tags=['Group Contract Operations'])
async def get_booking_policy(booking_policy_id: int, db: Session = Depends(get_db)):
    policy = crud.get_booking_policy(db, booking_policy_id=booking_policy_id)
    if not policy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking policy not found"
        )
    return policy


@router.post('/hotels/{hotel_id}/booking_policies', response_model=schemas.BookingPolicy,
             tags=['Group Contract Operations'])
async def create_booking_policy(booking_policy: schemas.BookingPolicyCreate, db: Session = Depends(get_db)):
    return crud.create_booking_policy(db, booking_policy=booking_policy)


# Room Type Operations
@router.get('/hotels/{hotel_id}/room_types', response_model=List[schemas.RoomType], tags=['Room Type Operations'])
async def read_room_types(hotel_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_room_types(db, hotel_id=hotel_id, skip=skip, limit=limit)


@router.post('/hotels/{hotel_id}/room_types', response_model=schemas.RoomType, tags=['Room Type Operations'])
async def create_room_type(hotel_id: int, room_type: schemas.RoomTypeCreate, db: Session = Depends(get_db)):
    return crud.create_room_type(db, room_type=room_type, hotel_id=hotel_id)


# Meal Option Operations
@router.get('/hotels/{hotel_id}/meal_options', response_model=List[schemas.MealOption], tags=['Meal Option Operations'])
async def get_meal_options(hotel_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_meal_options(db, hotel_id=hotel_id, skip=skip, limit=limit)


@router.post('/hotels/{hotel_id}/meal_options', response_model=schemas.MealOption, tags=['Meal Option Operations'])
async def create_meal_option(hotel_id: int, meal_option: schemas.MealOptionCreate, db: Session = Depends(get_db)):
    return crud.create_meal_option(db, meal_option=meal_option)


# Diving Package Operations
@router.get('/seasons/{season_id}/diving_packages', response_model=List[schemas.DivingPackage],
            tags=['Diving Package Operations'])
async def get_diving_packages(season_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_diving_packages(db, skip=skip, limit=limit)


@router.post('/seasons/{season_id}/diving_packages', response_model=schemas.DivingPackage,
             tags=['Diving Package Operations'])
async def create_diving_package(season_id: int, diving_package: schemas.DivingPackageCreate,
                                db: Session = Depends(get_db)):
    return crud.create_diving_package(db, diving_package=diving_package)


# Special Offer Operations
@router.get('/hotels/{hotel_id}/special_offers', response_model=List[schemas.SpecialOffer],
            tags=['Special Offer Operations'])
async def get_special_offers(hotel_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_special_offers(db, hotel_id=hotel_id, skip=skip, limit=limit)


@router.post('/hotels/{hotel_id}/special_offers', response_model=schemas.SpecialOffer,
             tags=['Special Offer Operations'])
async def create_special_offer(hotel_id: int, special_offer: schemas.SpecialOfferCreate, db: Session = Depends(get_db)):
    return crud.create_special_offer(db, special_offer=special_offer)


# Group Contract Operations
@router.get('/hotels/{hotel_id}/group_contracts', response_model=List[schemas.GroupContract],
            tags=['Group Contract Operations'])
async def get_group_contracts(hotel_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_group_contracts(db, hotel_id=hotel_id, skip=skip, limit=limit)


@router.post('/hotels/{hotel_id}/group_contracts', response_model=schemas.GroupContract,
             tags=['Group Contract Operations'])
async def create_group_contract(hotel_id: int, group_contract: schemas.GroupContractCreate,
                                db: Session = Depends(get_db)):
    return crud.create_group_contract(db, group_contract=group_contract)


# Occupancy Rate Operations
@router.get('/room_types/{room_type_id}/seasons/{season_id}/occupancy_rates',
            response_model=List[schemas.OccupancyRate], tags=['Occupancy Rate Operations'])
async def get_occupancy_rates(room_type_id: int, season_id: int, skip: int = 0, limit: int = 100,
                              db: Session = Depends(get_db)):
    return crud.get_occupancy_rates(db, room_type_id=room_type_id, season_id=season_id, skip=skip, limit=limit)


@router.post('/occupancy_rates', response_model=schemas.OccupancyRate, tags=['Occupancy Rate Operations'])
async def create_occupancy_rate(occupancy_rate: schemas.OccupancyRateCreate, db: Session = Depends(get_db)):
    return crud.create_occupancy_rate(db, occupancy_rate=occupancy_rate)


# Season Operations
@router.get('/hotels/{hotel_id}/seasons', response_model=List[schemas.Season], tags=['Season Operations'])
async def get_seasons(hotel_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_seasons(db, hotel_id=hotel_id, skip=skip, limit=limit)


@router.post('/hotels/{hotel_id}/seasons', response_model=schemas.Season, tags=['Season Operations'])
async def create_season(hotel_id: int, season: schemas.SeasonCreate, db: Session = Depends(get_db)):
    return crud.create_season(db, season=season)
