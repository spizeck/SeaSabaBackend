from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


def get_hotel(db: Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()


def get_hotels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()


def create_hotel(db: Session, hotel: schemas.HotelCreate):
    db_hotel = models.Hotel(**hotel.model_dump())
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel


def get_diving_package(db: Session, diving_package_id: int):
    return db.query(models.DivingPackage).filter(models.DivingPackage.id == diving_package_id).first()


def get_diving_packages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DivingPackage).offset(skip).limit(limit).all()


def create_diving_package(db: Session, diving_package: schemas.DivingPackageCreate):
    db_diving_package = models.DivingPackage(**diving_package.model_dump())
    db.add(db_diving_package)
    db.commit()
    db.refresh(db_diving_package)
    return db_diving_package


def get_room_type(db: Session, room_type_id: int):
    return db.query(models.RoomType).filter(models.RoomType.id == room_type_id).first()


def get_room_types(db: Session, hotel_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.RoomType).filter(models.RoomType.hotel_id == hotel_id).offset(skip).limit(limit).all()


def create_room_type(db: Session, room_type: schemas.RoomTypeCreate, hotel_id: int):
    db_room_type = models.RoomType(**room_type.model_dump(), hotel_id=hotel_id)
    db.add(db_room_type)
    db.commit()
    db.refresh(db_room_type)
    return db_room_type


def get_meal_option(db: Session, meal_option_id: int):
    return db.query(models.MealOption).filter(models.MealOption.id == meal_option_id).first()


def get_meal_options(db: Session, hotel_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.MealOption).filter(models.MealOption.hotel_id == hotel_id).offset(skip).limit(limit).all()


def create_meal_option(db: Session, meal_options: schemas.MealOptionCreate, hotel_id: int):
    db_meal_options = models.MealOption(**meal_options.model_dump())
    db.add(db_meal_options)
    db.commit()
    db.refresh(db_meal_options)
    return db_meal_options


def get_special_offer(db: Session, special_offer_id: int):
    return db.query(models.SpecialOffer).filter(models.SpecialOffer.id == special_offer_id).first()


def get_special_offers(db: Session, hotel_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.SpecialOffer).filter(models.SpecialOffer.hotel_id == hotel_id).offset(skip).limit(limit).all()


def create_special_offer(db: Session, special_offer: schemas.SpecialOfferCreate, hotel_id: int):
    db_special_offer = models.SpecialOffer(**special_offer.model_dump())
    db.add(db_special_offer)
    db.commit()
    db.refresh(db_special_offer)
    return db_special_offer


def get_booking_policy(db: Session, booking_policy_id: int):
    return db.query(models.BookingPolicy).filter(models.BookingPolicy.id == booking_policy_id).first()


def get_booking_policies(db: Session, hotel_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.BookingPolicy).filter(models.BookingPolicy.hotel_id == hotel_id).offset(skip).limit(limit).all()


def create_booking_policy(db: Session, booking_policy: schemas.BookingPolicyCreate, hotel_id: int):
    db_booking_policy = models.BookingPolicy(**booking_policy.model_dump())
    db.add(db_booking_policy)
    db.commit()
    db.refresh(db_booking_policy)
    return db_booking_policy


def get_season(db: Session, season_id: int):
    return db.query(models.Season).filter(models.Season.id == season_id).first()


def get_seasons(db: Session, hotel_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Season).filter(models.Season.hotel_id == hotel_id).offset(skip).limit(limit).all()


def create_season(db: Session, season: schemas.SeasonCreate, hotel_id: int):
    db_season = models.Season(**season.model_dump())
    db.add(db_season)
    db.commit()
    db.refresh(db_season)
    return db_season


def get_occupancy_rate(db: Session, occupancy_rate_id: int):
    return db.query(models.OccupancyRate).filter(models.OccupancyRate.id == occupancy_rate_id).first()


def get_occupancy_rates(db: Session, room_type_id: int, season_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.OccupancyRate)\
             .filter(models.OccupancyRate.room_type_id == room_type_id)\
             .filter(models.OccupancyRate.season_id == season_id)\
             .offset(skip).limit(limit).all()


def create_occupancy_rate(db: Session, occupancy_rate: schemas.OccupancyRateCreate):
    db_occupancy_rate = models.OccupancyRate(**occupancy_rate.model_dump())
    db.add(db_occupancy_rate)
    db.commit()
    db.refresh(db_occupancy_rate)
    return db_occupancy_rate


def get_group_contract(db: Session, group_contract_id: int):
    return db.query(models.GroupContract).filter(models.GroupContract.id == group_contract_id).first()


def get_group_contracts(db: Session, hotel_id: int = None, group_name: str = None,
                        customer: str = None, start_date: str = None, travel_agent: str = None,
                        skip: int = 0, limit: int = 10):
    query = db.query(models.GroupContract)

    if hotel_id is not None:
        query = query.filter(models.GroupContract.hotel_id == hotel_id)
    if group_name is not None:
        query = query.filter(
            models.GroupContract.group_name.ilike(f'%{group_name}%'))
    if customer is not None:
        query = query.filter(
            models.GroupContract.customer.ilike(f'%{customer}%'))
    if start_date is not None:
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            query = query.filter(
                models.GroupContract.start_date == start_date_obj)
        except ValueError:
            # Handle or log the incorrect date format
            pass
    if travel_agent is not None:
        query = query.filter(
            models.GroupContract.travel_agent.ilike(f'%{travel_agent}%'))

    return query.offset(skip).limit(limit).all()


def create_group_contract(db: Session, group_contract: schemas.GroupContractCreate):
    db_group_contract = models.GroupContract(**group_contract.model_dump())
    db.add(db_group_contract)
    db.commit()
    db.refresh(db_group_contract)
    return db_group_contract
