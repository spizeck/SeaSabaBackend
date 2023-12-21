from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from enum import Enum


# Enum for OccupancyType
class OccupancyType(str, Enum):
    SINGLE = 'single'
    DOUBLE = 'double'
    TRIPLE = 'triple'
    QUADRUPLE = 'quadruple'


# Base Models
class HotelBase(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    contact_info: Optional[str] = None
    amenities: Optional[str] = None
    policies: Optional[str] = None


class MealOptionBase(BaseModel):
    hotel_id: int
    name: str
    description: Optional[str] = None
    price: float


class RoomTypeBase(BaseModel):
    hotel_id: int
    name: str
    number_of_rooms: Optional[int] = None


class OccupancyRateBase(BaseModel):
    room_type_id: int
    season_id: int
    occupancy_type: OccupancyType
    rate: float


class DivingPackageBase(BaseModel):
    season_id: int
    name: str
    price: float


class SpecialOfferBase(BaseModel):
    hotel_id: int
    name: str
    description: Optional[str] = None


class BookingPolicyBase(BaseModel):
    hotel_id: int
    name: str
    policy_text: Optional[str] = None


class GroupContractBase(BaseModel):
    hotel_id: int
    group_name: str
    customer: str
    start_date: date
    end_date: date
    travel_agent: Optional[str] = None
    contract: Optional[str] = None


class SeasonBase(BaseModel):
    hotel_id: int
    name: str
    start_date: date
    end_date: date


# Create Schemas
class HotelCreate(HotelBase):
    name: str


class MealOptionCreate(MealOptionBase):
    pass


class RoomTypeCreate(RoomTypeBase):
    pass


class OccupancyRateCreate(OccupancyRateBase):
    pass


class DivingPackageCreate(DivingPackageBase):
    pass


class SpecialOfferCreate(SpecialOfferBase):
    pass


class BookingPolicyCreate(BookingPolicyBase):
    pass


class GroupContractCreate(GroupContractBase):
    pass


class SeasonCreate(SeasonBase):
    pass


# Extended Schemas with IDs
class OccupancyRate(OccupancyRateBase):
    id: int


class RoomType(RoomTypeBase):
    id: int
    occupancy_rates: List[OccupancyRate]


class MealOption(MealOptionBase):
    id: int


class DivingPackage(DivingPackageBase):
    id: int


class Season(SeasonBase):
    id: int
    diving_packages: List[DivingPackage]


class SpecialOffer(SpecialOfferBase):
    id: int


class BookingPolicy(BookingPolicyBase):
    id: int


class GroupContract(GroupContractBase):
    id: int


class Hotel(HotelBase):
    id: int
    room_types: List[RoomType]
    meal_options: List[MealOption]
    special_offers: List[SpecialOffer]
    booking_policies: List[BookingPolicy]
    group_contracts: List[GroupContract]
    is_active: bool


# Update Schemas
class HotelUpdate(HotelBase):
    is_active: Optional[bool] = None


class RoomTypeUpdate(RoomTypeBase):
    pass


class MealOptionUpdate(MealOptionBase):
    pass


class OccupancyRateUpdate(OccupancyRateBase):
    pass


class DivingPackageUpdate(DivingPackageBase):
    pass


class SpecialOfferUpdate(SpecialOfferBase):
    pass


class BookingPolicyUpdate(BookingPolicyBase):
    pass


class GroupContractUpdate(GroupContractBase):
    pass


class SeasonUpdate(SeasonBase):
    pass
