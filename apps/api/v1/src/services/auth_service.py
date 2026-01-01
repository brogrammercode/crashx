from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.user_repository import UserRepository
from src.models.user import User
from src.schemas import user as user_schema
from src.core.security import get_password_hash, verify_password

class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def authenticate(self, email: str, password: str) -> Optional[User]:
        user = await self.repo.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def register(self, user_in: user_schema.UserCreate) -> User:
        existing_user = await self.repo.get_by_email(user_in.email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        hashed_password = get_password_hash(user_in.password)
        db_obj = {
            "email": user_in.email,
            "hashed_password": hashed_password,
            "full_name": user_in.full_name,
            "is_active": True
        }
        return await self.repo.create(db_obj)
