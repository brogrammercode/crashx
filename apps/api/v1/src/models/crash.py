import enum
from sqlalchemy import Column, String, ForeignKey, Enum, Text, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.core.database import Base
from src.models.base_mixins import UUIDModel

class Severity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Status(str, enum.Enum):
    OPEN = "open"
    RESOLVED = "resolved"
    IGNORED = "ignored"

class Crash(Base, UUIDModel):
    __tablename__ = "crashes"

    error_message = Column(String, nullable=False)
    stack_trace = Column(Text, nullable=False)
    device_info = Column(JSON, nullable=True) # e.g. {"os": "android", "version": "14"}
    app_version = Column(String, nullable=True)
    
    severity = Column(Enum(Severity), default=Severity.MEDIUM)
    status = Column(Enum(Status), default=Status.OPEN)
    
    occurred_at = Column(DateTime(timezone=True), nullable=False) # When the crash actually happened on device

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)

    # Relationships
    project = relationship("Project", backref="crashes")
