from typing import Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime, timezone
from uuid import UUID
from enum import Enum

class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CrashCreate(BaseModel):
    error_message: str
    stack_trace: str
    device_info: Optional[Dict[str, Any]] = None
    app_version: Optional[str] = None
    severity: Severity = Severity.MEDIUM
    occurred_at: datetime = datetime.now(timezone.utc)

class CrashInDB(CrashCreate):
    id: UUID
    project_id: UUID
    status: str
    
    class Config:
        from_attributes = True

class Crash(CrashInDB):
    pass
