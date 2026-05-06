from fastapi import APIRouter, UploadFile, File, Form
from app.services.face_service import enroll_face, recognize_face

router = APIRouter()

@router.post("/enroll")
async def enroll(
    person_name: str = Form(...),
    file: UploadFile = File(...)
):
    return await enroll_face(file, person_name)


@router.post("/recognize")
async def recognize(
    file: UploadFile = File(...),
    threshold: float = Form(0.5)
):
    return await recognize_face(file, threshold)
