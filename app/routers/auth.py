from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import Token
from app.crud import user as user_crud
from app.core.security import create_access_token, decode_token

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", auto_error=True)


@router.post("/register", response_model=UserResponse)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if user_crud.get_by_username(db, payload.username):
        raise HTTPException(status_code=400, detail="Username already taken")
    if user_crud.get_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = user_crud.create(db, username=payload.username, email=payload.email, full_name=payload.full_name, password=payload.password, is_active=payload.is_active)
    return user


@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2 form fields: username, password
    user = user_crud.authenticate(db, form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password"
        )
    token = create_access_token(subject=user.username)
    return {"access_token": token, "token_type": "Bearer"}


@router.get("/me", response_model=UserResponse)
def me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_token(token)
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    user = user_crud.get_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
