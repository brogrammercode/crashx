from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.project import Project
from src.repositories.base_repository import BaseRepository
from sqlalchemy.dialects.postgresql import UUID

class ProjectRepository(BaseRepository[Project]):
    def __init__(self, db: AsyncSession):
        super().__init__(Project, db)

    async def get_by_api_key(self, api_key: str) -> Optional[Project]:
        query = select(Project).where(Project.api_key == api_key)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_by_user(self, user_id: UUID) -> List[Project]:
        query = select(Project).where(Project.user_id == user_id)
        result = await self.db.execute(query)
        return result.scalars().all()
