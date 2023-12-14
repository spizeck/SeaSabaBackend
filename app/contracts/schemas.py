from pydantic import BaseModel
from typing import List, Optional
from datetime import date


# Base Schemas


class HotelBase(BaseModel):
    name: str
    location: str
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
    description: Optional[str] = None


class OccupancyRateBase(BaseModel):
    room_type_id: int
    season_id: int
    occupancy_type: str  # e.g., 'single', 'double'
    rate: float


class DivingPackageBase(BaseModel):
    season_id: int
    name: str
    price: float
    foc_slots: Optional[int] = 0


class SpecialOfferBase(BaseModel):
    hotel_id: int
    name: str
    description: str


class BookingPolicyBase(BaseModel):
    hotel_id: int
    name: str
    policy_text: str


class GroupContractBase(BaseModel):
    hotel_id: int
    group_name: str
    customer: str
    start_date: date
    end_date: date
    travel_agent: Optional[str] = None
    contract: str


class SeasonBase(BaseModel):
    hotel_id: int
    name: str
    start_date: date
    end_date: date
    hotel_foc_slots: Optional[str] = None
    diving_foc_slots: Optional[str] = None


# Create Schemas


class HotelCreate(HotelBase):
    pass


class RoomTypeCreate(RoomTypeBase):
    pass


class MealOptionCreate(MealOptionBase):
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
    seasons: List[Season]
