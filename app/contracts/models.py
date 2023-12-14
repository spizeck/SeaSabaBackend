from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    description = Column(String, nullable=True)
    contact_info = Column(String, nullable=True)
    amenities = Column(String, nullable=True)
    policies = Column(String, nullable=True)
    
    meal_options = relationship('MealOption', back_populates='hotel')
    room_types = relationship('RoomType', back_populates='hotel')
    special_offers = relationship('SpecialOffer', back_populates='hotel')
    booking_policies = relationship('BookingPolicy', back_populates='hotel')
    group_contracts = relationship('GroupContract', back_populates='hotel')


class MealOption(Base):
    __tablename__ = 'meal_options'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    hotel = relationship('Hotel', back_populates='meal_options')


class RoomType(Base):
    __tablename__ = 'room_types'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, index=True)
    number_of_rooms = Column(Integer, nullable=True)
    
    hotel = relationship('Hotel', back_populates='room_types')
    occupancy_rates = relationship(
        'OccupancyRate')


class OccupancyRate(Base):
    __tablename__ = 'occupancy_rates'

    id = Column(Integer, primary_key=True, index=True)
    room_type_id = Column(Integer, ForeignKey('room_types.id'))
    season_id = Column(Integer, ForeignKey('seasons.id'))
    occupancy_type = Column(String)  # e.g., 'single', 'double', etc.
    rate = Column(Float)
    
    room_type = relationship('RoomType', back_populates='occupancy_rates')
    season = relationship('Season', back_populates='occupancy_rates')


class DivingPackage(Base):
    __tablename__ = 'diving_packages'

    id = Column(Integer, primary_key=True, index=True)
    season_id = Column(Integer, ForeignKey('seasons.id'))
    name = Column(String, index=True)
    price = Column(Float)
    
    seasons = relationship('Season', back_populates='diving_packages')


class SpecialOffer(Base):
    __tablename__ = 'special_offers'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, index=True)
    description = Column(String)
    hotel = relationship('Hotel', back_populates='special_offers')


class BookingPolicy(Base):
    __tablename__ = 'booking_policies'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, index=True)
    policy_text = Column(String)
    hotel = relationship('Hotel', back_populates='booking_policies')


class GroupContract(Base):
    __tablename__ = 'group_contracts'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    group_name = Column(String, index=True)
    customer = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    travel_agent = Column(String, nullable=True)
    contract = Column(String)
    hotel = relationship('Hotel', back_populates='group_contracts')
    diving_package_id = Column(Integer, ForeignKey('diving_packages.id'))
    diving_package = relationship('DivingPackage')


class Season(Base):
    __tablename__ = 'seasons'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    name = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    hotel_foc_slots = Column(String, nullable=True)
    diving_foc_slots = Column(String, nullable=True)
    
    hotel = relationship('Hotel', back_populates='seasons')
    occupancy_rates = relationship('OccupancyRate', back_populates='season')
    diving_packages = relationship('DivingPackage', back_populates='season')
