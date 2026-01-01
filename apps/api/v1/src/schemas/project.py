from typing import Optional
from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    discord_webhook_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: UUID
    user_id: UUID
    api_key: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Project(ProjectInDBBase):
    pass
