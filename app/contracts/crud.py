from sqlalchemy.orm import Session
from app.contracts import models, schemas

def get_hotel(db : Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()

def get_hotels(db : Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()

def create_hotel(db : Session, hotel: schemas.HotelCreate):
    db_hotel = models.Hotel(**hotel.model_dump())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

def get_room_type(db : Session, room_type_id: int):
    return db.query(models.RoomType).filter(models.RoomType.id == room_type_id).first()

def create_room_type(db : Session, room_type: schemas.RoomTypeCreate, hotel_id: int):
    db_room_type = models.RoomType(**room_type.model_dump(), hotel_id=hotel_id)
    db.add(db_room_type)
    db.commit()
    db.refresh(db_room_type)
    return db_room_type

def get_diving_package(db : Session, diving_package_id: int):