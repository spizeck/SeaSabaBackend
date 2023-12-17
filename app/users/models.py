from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    profile = relationship('UserProfile', back_populates='user',
                           uselist=False, cascade='all, delete-orphan')
    preferences = relationship(
        'UserPreferences', back_populates='user', uselist=False, cascade='all, delete-orphan')


class UserProfile(Base):
    __tablename__ = 'user_profiles'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    first_name = Column(String, default="")
    last_name = Column(String, default="")
    phone_number = Column(String, default="")
    company_name = Column(String, default="")

    user = relationship('User', back_populates='profile')


class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='preferences')

    # TODO: Define specific user preferences in the UserPreferences model and schema.
