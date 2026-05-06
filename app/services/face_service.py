import cv2
import numpy as np
import uuid
from fastapi import HTTPException
from qdrant_client.models import PointStruct
from app.core.config import settings
import os
from app.ml.face_model import app
from app.db.qdrant_client import client, collection_name
from app.utils.file_utils import save_file


# -----------------------
# ENROLL API LOGIC
# -----------------------
async def enroll_face(file, person_name: str):

    image_path = save_file(file, "enroll")

    image = cv2.imread(image_path)

    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image")

    faces = app.get(image)

    if len(faces) == 0:
        raise HTTPException(status_code=400, detail="No face detected")

    face = faces[0]

    embedding = face.embedding
    embedding = embedding / np.linalg.norm(embedding)

    point_id = str(uuid.uuid4())

    filename = os.path.basename(image_path)
    image_url = f"{settings.BASE_URL}/media/enroll/{filename}"

    payload = {
        "person_name": person_name,
        # "image_path": image_path
        "image_path": image_url
    }

    point = PointStruct(
        id=point_id,
        vector=embedding.tolist(),
        payload=payload
    )

    client.upsert(
        collection_name=collection_name,
        points=[point]
    )

    return {
        "message": "Face enrolled successfully",
        "person_name": person_name,
        "point_id": point_id
    }


# -----------------------
# RECOGNIZE API LOGIC
# -----------------------
async def recognize_face(file, threshold: float = 0.5):

    image_path = save_file(file, "recognize")

    image = cv2.imread(image_path)

    if image is None:
        raise HTTPException(status_code=400, detail="Invalid image")

    faces = app.get(image)

    if len(faces) == 0:
        raise HTTPException(status_code=400, detail="No face detected")

    face = faces[0]

    embedding = face.embedding
    embedding = embedding / np.linalg.norm(embedding)

    search_result = client.query_points(
        collection_name=collection_name,
        query=embedding.tolist(),
        limit=1
    )

    if len(search_result.points) == 0:
        return {
            "message": "No match found"
        }

    result = search_result.points[0]

    similarity_score = result.score
    person_name = result.payload["person_name"]

    if similarity_score >= threshold:
        return {
            "recognized": True,
            "person_name": person_name,
            "similarity_score": similarity_score
        }
    else:
        return {
            "recognized": False,
            "person_name": None,
            "similarity_score": similarity_score
        }
