import httpx
from src.schemas.crash import CrashCreate
from src.models.project import Project

class DiscordService:
    @staticmethod
    async def send_crash_alert(webhook_url: str, crash_data: CrashCreate, project_name: str):
        if not webhook_url:
            return

        color_map = {
            "low": 0x3498db,      # Blue
            "medium": 0xf1c40f,   # Yellow
            "high": 0xe67e22,     # Orange
            "critical": 0xe74c3c  # Red
        }

        embed = {
            "title": f"🚨 Crash in {project_name}",
            "description": f"**Error**: {crash_data.error_message}",
            "color": color_map.get(crash_data.severity.value, 0x000000),
            "fields": [
                {"name": "Severity", "value": crash_data.severity.value.upper(), "inline": True},
                {"name": "App Version", "value": crash_data.app_version or "Unknown", "inline": True},
                {"name": "Device", "value": str(crash_data.device_info) if crash_data.device_info else "Unknown", "inline": False},
                {"name": "Stack Trace", "value": f"```{crash_data.stack_trace[:1000]}```"}
            ],
            "footer": {"text": "CrashX Analytics"}
        }

        payload = {
            "embeds": [embed]
        }

        async with httpx.AsyncClient() as client:
            try:
                await client.post(webhook_url, json=payload)
            except Exception as e:
                print(f"Failed to send Discord webhook: {e}")
