from dotenv import load_dotenv
import os
load_dotenv()

class Settings:
    QDRANT_URL = os.getenv("QDRANT_URL", "http://192.168.1.190:6333")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "FaceRecognition")
    VECTOR_SIZE = 512
    
    BASE_URL = os.getenv("BASE_URL", "http://192.168.1.80:8080")

settings = Settings()
