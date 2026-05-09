from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router as face_router
from app.frontend.routes import router as frontend_router

app = FastAPI(title="Face Recognition API")

app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(frontend_router, tags=["Frontend"])
app.include_router(face_router, prefix="/api/v1/face", tags=["Face"])
