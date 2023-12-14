from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class HotelBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None
    contact_info: Optional[str] = None
    amenities: Optional[str] = None
    policies: Optional[str] = None
    foc_slots: Optional[int] = None


class MealOptionBase(BaseModel):
    hotel_id: int
    name: str
    description: Optional[str] = None
    price: float


class RoomTypeBase(BaseModel):
    hotel_id: int
    name: str
    description: Optional[str] = None
    number_of_rooms: Optional[int] = None


class RoomRateBase(BaseModel):
    hotel_id: int
    room_type_id: int
    season_id: int
    rate: float


class OccupancyRateBase(BaseModel):
    occupancy_type: str  # e.g., 'single', 'double'
    rate: float


class DivingPackageBase(BaseModel):
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


class HotelCreate(HotelBase):
    pass


class RoomTypeCreate(RoomTypeBase):
    hotel_id: int


class MealOptionCreate(MealOptionBase):
    hotel_id: int


class DivingPackageCreate(DivingPackageBase):
    pass


class GroupContractCreate(GroupContractBase):
    pass


class OccupancyRate(OccupancyRateBase):
    id: int


class RoomRate(RoomRateBase):
    id: int
    season_id: int


class RoomType(RoomTypeBase):
    id: int
    hotel_id: int
    occupancy_rates: List[OccupancyRate]
    room_rates: List[RoomRate]


class MealOption(MealOptionBase):
    id: int
    hotel_id: int


class Season(SeasonBase):
    id: int
    hotel_id: int
    room_rates: List[RoomRate]


class DivingPackage(DivingPackageBase):
    id: int


class SpecialOffer(SpecialOfferBase):
    id: int
    hotel_id: int


class BookingPolicy(BookingPolicyBase):
    id: int
    hotel_id: int


class GroupContract(GroupContractBase):
    id: int
    hotel_id: int


class Hotel(HotelBase):
    id: int
    room_types: List[RoomType]
    meal_options: List[MealOption]
    special_offers: List[SpecialOffer]
    booking_policies: List[BookingPolicy]
    group_contracts: List[GroupContract]
    seasons: List[Season]
