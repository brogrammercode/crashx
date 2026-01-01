from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.crash import Crash
from src.repositories.base_repository import BaseRepository
from sqlalchemy.dialects.postgresql import UUID

class CrashRepository(BaseRepository[Crash]):
    def __init__(self, db: AsyncSession):
        super().__init__(Crash, db)

    async def get_project_crashes(self, project_id: UUID, skip: int = 0, limit: int = 100) -> List[Crash]:
        query = select(Crash).where(Crash.project_id == project_id).offset(skip).limit(limit)
        result = await self.db.execute(query)
        return result.scalars().all()
