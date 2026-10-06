from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.security import create_access_token, hash_password, verify_password
from ..database import get_db
from ..models.driver import Driver
from ..models.user import User
from ..schemas.auth import AuthResponse, LoginRequest, RegisterRequest

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) -> AuthResponse:
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    user = User(email=payload.email, hashed_password=hash_password(payload.password), name=payload.name)
    db.add(user)
    db.flush()
    db.add(Driver(user_id=user.id, name=payload.name))
    db.commit()
    token = create_access_token(user.email)
    return AuthResponse(access_token=token, user={"id": user.id, "email": user.email, "name": user.name})


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> AuthResponse:
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token(user.email)
    return AuthResponse(access_token=token, user={"id": user.id, "email": user.email, "name": user.name})
