from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.project_repository import ProjectRepository
from src.repositories.crash_repository import CrashRepository
from src.models.crash import Crash
from src.services.discord_service import DiscordService
from src.schemas import crash as crash_schema
from fastapi import BackgroundTasks

class CrashService:
    def __init__(self, db: AsyncSession):
        self.project_repo = ProjectRepository(db)
        self.crash_repo = CrashRepository(db)

    async def report_crash(self, api_key: str, crash_in: crash_schema.CrashCreate, background_tasks: BackgroundTasks):
        # 1. Validate API Key
        project = await self.project_repo.get_by_api_key(api_key)
        if not project:
            raise ValueError("Invalid API Key")

        # 2. Save Crash
        crash_data = crash_in.dict()
        crash_data["project_id"] = project.id
        crash = await self.crash_repo.create(crash_data)

        # 3. Trigger Discord Notification (Background)
        if project.discord_webhook_url:
            background_tasks.add_task(
                DiscordService.send_crash_alert,
                project.discord_webhook_url,
                crash_in,
                project.name
            )

        return crash
