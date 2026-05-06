from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from app.core.config import settings

# collection_name = "FaceRecognition"
collection_name = settings.COLLECTION_NAME

client = QdrantClient(
    url="http://192.168.1.190:6333"
)

# Create collection if not exists
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=512,
            distance=Distance.COSINE
        )
    )
