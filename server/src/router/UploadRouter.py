import sys
import uuid
import os
from fastapi import APIRouter, UploadFile


from src.service.DexParser.DexParser import DexPaser


router = APIRouter()


@router.post("/upload/apk")
async def uploadApk(file: UploadFile):
    UPLOAD_DIR = "."

    content = await file.read()
    filename = f"{str(uuid.uuid4())}.apk"

    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content)  

    return {"filename": filename}