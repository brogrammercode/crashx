from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.core.database import Base
from src.models.base_mixins import UUIDModel, TimeStampedModel

class Project(Base, UUIDModel, TimeStampedModel):
    __tablename__ = "projects"

    name = Column(String, nullable=False)
    api_key = Column(String, unique=True, index=True, nullable=False)
    discord_webhook_url = Column(String, nullable=True)
    
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # Relationships
    user = relationship("User", backref="projects")
