from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table, Date
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
    foc_slots = Column(Integer, nullable=True)

    meal_options = relationship('MealOption', back_populates='hotel')
    room_types = relationship('RoomType', back_populates='hotel')
    meal_packages = relationship('MealPackage', back_populates='hotel')
    special_offers = relationship('SpecialOffer', back_populates='hotel')
    booking_policies = relationship('BookingPolicy', back_populates='hotel')
    group_contracts = relationship('GroupContract', back_populates='hotel')
    seasons = relationship('Season', back_populates='hotel')


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
        'OccupancyRate', secondary='room_type_occupancy_rate_association')
    room_rates = relationship('RoomRate', back_populates='room_type')


class RoomRate(Base):
    __tablename__ = 'room_rates'

    id = Column(Integer, primary_key=True, index=True)
    room_type_id = Column(Integer, ForeignKey('room_types.id'))
    season_id = Column(Integer, ForeignKey('seasons.id'))
    rate = Column(Float)
    room_type = relationship('RoomType', back_populates='room_rates')
    season = relationship('Season', back_populates='room_rates')


class OccupancyRate(Base):
    __tablename__ = 'occupancy_rates'

    id = Column(Integer, primary_key=True, index=True)
    occupancy_type = Column(String)  # e.g., 'single', 'double', etc.
    rate = Column(Float)


class DivingPackage(Base):
    __tablename__ = 'diving_packages'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    foc_slots = Column(Integer, default=0)


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
    hotel = relationship('Hotel', back_populates='seasons')
    room_rates = relationship('RoomRate', back_populates='season')


room_type_occupancy_rate_association = Table(
    'room_type_occupancy_rate_association', Base.metadata,
    Column('room_type_id', ForeignKey('room_types.id')),
    Column('occupancy_rate_id', ForeignKey('occupancy_rates.id'))
)

diving_package_season_association = Table(
    'diving_package_season_association', Base.metadata,
    Column('diving_package_id', ForeignKey('diving_packages.id')),
    Column('season_id', ForeignKey('seasons.id')),
    Column('foc_terms', Integer)
)
