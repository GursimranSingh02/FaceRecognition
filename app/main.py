from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

app = FastAPI(title="Face Recognition API")

app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(router, prefix="/api/v1/face", tags=["Face"])
