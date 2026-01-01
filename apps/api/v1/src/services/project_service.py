import secrets
from uuid import UUID
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.project_repository import ProjectRepository
from src.schemas import project as project_schema

class ProjectService:
    def __init__(self, db: AsyncSession):
        self.repo = ProjectRepository(db)

    async def create_project(self, project_in: project_schema.ProjectCreate, user_id: UUID) -> object:
        # Generate API Key
        api_key = f"cx_{secrets.token_urlsafe(32)}"
        
        obj_in = project_in.dict()
        obj_in["user_id"] = user_id
        obj_in["api_key"] = api_key
        
        return await self.repo.create(obj_in)

    async def get_user_projects(self, user_id: UUID) -> List[object]:
        return await self.repo.get_by_user(user_id)
