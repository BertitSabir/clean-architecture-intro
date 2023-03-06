from fastapi import FastAPI

from application.config import get_settings
from application.rest import room

settings = get_settings()

# Core Application Instance
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
)

# Add Routers
app.include_router(room.room_router, tags=["rooms"])
