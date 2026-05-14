from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from app.core.config import settings

# collection_name = "FaceRecognition"
collection_name = settings.COLLECTION_NAME
qdrant_api_key = settings.QDRANT_CLOUD_API_KEY
qdrant_url = settings.QDRANT_CLOUD_URL

# client = QdrantClient(
#     # url="http://192.168.1.190:6333"
#     host="localhost",
#     port=6333,
# )

client = QdrantClient(
    url=qdrant_url, 
    api_key=qdrant_api_key
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
