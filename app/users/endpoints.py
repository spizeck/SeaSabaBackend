from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import UserCreate, User, UpdateUser
from .crud import get_user_by_email, create_user, get_user_by_username, get_user, update_user, delete_user
from app.dependencies import get_db

router = APIRouter()


@router.post("/users/", response_model=User, tags=["User Operations"])
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

@router.get("/users/{user_id}/", response_model=User, tags=["User Operations"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.put("/users/{user_id}/", response_model=User, tags=["User Operations"])
def update_user_endpoint(user_id: int, user_update: UpdateUser, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = update_user(db=db, db_user=db_user, user_update=user_update)
    return updated_user

@router.delete("/users/{user_id}/", response_model=bool, tags=["User Operations"])
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db=db, user_id=user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return True
