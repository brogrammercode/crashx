from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.services.project_service import ProjectService
from src.schemas import project as project_schema
from src.models.user import User
from src.controllers.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=project_schema.Project)
async def create_project(
    project_in: project_schema.ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = ProjectService(db)
    return await service.create_project(project_in, current_user.id)

@router.get("/", response_model=List[project_schema.Project])
async def read_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = ProjectService(db)
    return await service.get_user_projects(current_user.id)
