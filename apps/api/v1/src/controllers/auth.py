from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.services.auth_service import AuthService
from src.schemas import user as user_schema
from src.schemas.token import Token
from src.core import security

router = APIRouter()

@router.post("/register", response_model=user_schema.User)
async def register(user_in: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    auth_service = AuthService(db)
    try:
        user = await auth_service.register(user_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.post("/login", response_model=Token)
async def login(user_in: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    auth_service = AuthService(db)
    user = await auth_service.authenticate(user_in.email, user_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(subject=user.id)
    return {"access_token": access_token, "token_type": "bearer"}
