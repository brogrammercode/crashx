from sqlalchemy import Column, String, Boolean
from src.core.database import Base
from src.models.base_mixins import UUIDModel, TimeStampedModel

class User(Base, UUIDModel, TimeStampedModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, nullable=True)
