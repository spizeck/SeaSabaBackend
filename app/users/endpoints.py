from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from .schemas import UserCreate, ReturnUser, UpdateUser, TokenData, UserPreferencesBase, UserProfileBase, UpdateUserStatus
from .crud import (get_user_by_email, create_user, get_user_by_username, get_user, update_user, delete_user,
                   update_user_preferences, update_user_profile, update_user_status, get_users)
from app.dependencies import get_db
from app.core.security import verify_password, create_access_token, get_current_user

router = APIRouter()


@router.post("/login", response_model=TokenData, tags=["Authentication"])
def login_user_endpoint(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = get_user_by_username(db, username=form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token, expire = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "exp": expire, "token_type": "bearer", "username": db_user.username}


@router.post('/token', response_model=TokenData, tags=['Authentication'])
def generate_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    return login_user_endpoint(db=db, form_data=form_data)


@router.get("/users/me/", response_model=ReturnUser, tags=["Authentication"])
def get_current_user_data(current_user: ReturnUser = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user


@router.post("/users/", response_model=ReturnUser, tags=["User Operations"])
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    if get_user_by_email(db, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    if get_user_by_username(db, username=user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    return create_user(db=db, user=user)


@router.get("/users/{user_id}/", response_model=ReturnUser, tags=["User Operations"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user


@router.get("/users/email/{email}/", response_model=ReturnUser, tags=["User Operations"])
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user


@router.get("/users/username/{username}/", response_model=ReturnUser, tags=["User Operations"])
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=username)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user


@router.get("/users/", response_model=List[ReturnUser], tags=["User Operations"])
def get_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db=db, skip=skip, limit=limit)
    return users


@router.put("/users/{user_id}/", response_model=ReturnUser, tags=["User Operations"])
def update_user_endpoint(user_id: int, user_update: UpdateUser, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = update_user(db=db, db_user=db_user, user_update=user_update)
    return updated_user


@router.put("/users/profile/{user_id}/", response_model=ReturnUser, tags=["User Operations"])
def update_user_profile_endpoint(user_id: int, user_profile: UserProfileBase, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = update_user_profile(db=db, db_user=db_user, user_update=user_profile)
    return updated_user


@router.put("/users/preferences/{user_id}/", response_model=UserPreferencesBase, tags=["User Operations"])
def update_user_preferences_endpoint(user_id: int, user_preferences: UserPreferencesBase, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = update_user_preferences(db=db, db_user=db_user, user_update=user_preferences)
    return updated_user


@router.delete("/users/{user_id}/", response_model=bool, tags=["User Operations"])
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db=db, user_id=user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return True


@router.put("/users/approve/{user_id}/", response_model=bool, tags=["User Operations"])
def approve_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user_status_update = UpdateUserStatus(is_active=True)
    update_user_status(db=db, db_user=db_user, user_update=user_status_update)
    return True


@router.put("/users/disapprove/{user_id}/", response_model=bool, tags=["User Operations"])
def disapprove_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user_status_update = UpdateUserStatus(is_active=False)
    update_user_status(db=db, db_user=db_user, user_update=user_status_update)
    return True


@router.put("/users/promote/{user_id}/", response_model=bool, tags=["User Operations"])
def promote_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    update_user_admin_status = UpdateUserStatus(is_admin=True)
    update_user_status(db=db, db_user=db_user, user_update=update_user_admin_status)
    return True


@router.put("/users/demote-admin/{user_id}/", response_model=bool, tags=["User Operations"])
def demote_admin_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    update_user_admin_status = UpdateUserStatus(is_admin=False)
    update_user_status(db=db, db_user=db_user, user_update=update_user_admin_status)
    return True
