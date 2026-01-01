from fastapi import APIRouter, Depends, Header, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.services.crash_service import CrashService
from src.schemas import crash as crash_schema

router = APIRouter()

@router.post("/report", response_model=crash_schema.Crash)
async def report_crash(
    crash_in: crash_schema.CrashCreate,
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    service = CrashService(db)
    try:
        crash = await service.report_crash(x_api_key, crash_in, background_tasks)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    return crash
