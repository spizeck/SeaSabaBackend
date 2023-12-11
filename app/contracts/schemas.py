from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Base schemas for simple fields
class HotelBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None
    contact_info: Optional[str] = None
    amenities: Optional[str] = None
    policies: Optional[str] = None
    foc_slots: Optional[int] = None

class OccupancyRateBase(BaseModel):
    occupancy_type: str  # e.g., 'single', 'double'
    rate: float

class RoomRateBase(BaseModel):
    rate: float

class RoomTypeBase(BaseModel):
    name: str
    number_of_rooms: int

class MealOptionBase(BaseModel):
    name: str
    description: str
    price: float

class SeasonBase(BaseModel):
    name: str
    start_date: date
    end_date: date

class DivingPackageBase(BaseModel):
    name: str
    price: float
    foc_slots: Optional[int] = 0

class SpecialOfferBase(BaseModel):
    name: str
    description: str

class BookingPolicyBase(BaseModel):
    name: str
    policy_text: str

class GroupContractBase(BaseModel):
    group_name: str
    customer: str
    start_date: date
    end_date: date
    travel_agent: Optional[str] = None
    contract: str

# Create Schemas (for POST requests)
class HotelCreate(HotelBase):
    pass

class RoomTypeCreate(RoomTypeBase):
    hotel_id: int

class MealOptionCreate(MealOptionBase):
    hotel_id: int

# ... similarly create 'Create' schemas for other models ...

# Full Schemas with Relationships
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

# ... other full schemas if needed ...
