from sqlalchemy.orm import Session
from app.users.models import User, UserProfile, UserPreferences
from app.users.schemas import UserCreate, UpdateUser
from app.core.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email,
                   hashed_password=hashed_password)
    db.add(db_user)
    db.commit()

    db_profile = UserProfile(user_id=db_user.id)
    db_preferences = UserPreferences(user_id=db_user.id)

    db.add(db_profile)
    db.add(db_preferences)
    db.commit()

    db.refresh(db_user)
    db.refresh(db_profile)
    db.refresh(db_preferences)

    # TODO: Implement account activation workflow using the is_active field in the User model.

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


def update_user(db: Session, db_user: User, user_update: UpdateUser):
    if user_update.username is not None:
        db_user.username = user_update.username
    if user_update.email is not None:
        db_user.email = user_update.email
    if user_update.password is not None:
        db_user.hashed_password = get_password_hash(user_update.password)

    db_profile = db.query(UserProfile).filter(
        UserProfile.user_id == db_user.id).first()
    if not db_profile:
        db_profile = UserProfile(user_id=db_user.id)
        db.add(db_profile)
    if user_update.first_name is not None:
        db_profile.first_name = user_update.first_name
    if user_update.last_name is not None:
        db_profile.last_name = user_update.last_name
    if user_update.phone_number is not None:
        db_profile.phone_number = user_update.phone_number
    if user_update.company_name is not None:
        db_profile.company_name = user_update.company_name

    db_preferences = db.query(UserPreferences).filter(
        UserPreferences.user_id == db_user.id).first()
    if not db_preferences:
        db_preferences = UserPreferences(user_id=db_user.id)
        db.add(db_preferences)

    db.commit()
    db.refresh(db_user)
    db.refresh(db_profile)
    db.refresh(db_preferences)
    return db_user
