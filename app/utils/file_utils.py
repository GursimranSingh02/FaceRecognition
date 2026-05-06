import os
import uuid

BASE_PATH = "media"

def save_file(upload_file, folder):
    folder_path = os.path.join(BASE_PATH, folder)
    os.makedirs(folder_path, exist_ok=True)

    filename = f"{uuid.uuid4()}.jpg"
    file_path = os.path.join(folder_path, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path
