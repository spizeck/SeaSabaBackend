from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.users.schemas import UserCreate, User, UpdateUser
from app.users.crud import get_user_by_email, create_user, get_user_by_username, get_user, update_user, delete_user
from app.dependencies import get_db
from app.core.security import verify_password, create_access_token, get_current_user
from app.users.schemas import TokenData

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
    return {"access_token": access_token, "exp": expire, "token_type": "bearer"}


@router.get("/users/me/", response_model=User, tags=["User Operations"])
def get_current_user_data(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user


@router.get("/users/{user_id}/", response_model=User, tags=["User Operations"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user


@router.get("/users/email/{email}/", response_model=User, tags=["User Operations"])
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user


@router.get("/users/username/{username}/", response_model=User, tags=["User Operations"])
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=username)
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
