from fastapi import UploadFile
import uuid
import os
import pickle

from src.repository.UploadFileMetaRepo import UploadFileMetaRepo
from src.util.Singleton import Singleton

class FileManageService(Singleton):

    def __init__(self) -> None:
        self.APK_DIR = "./apk"
        self.UploadFileMetaRepo = UploadFileMetaRepo()


    async def uploadApk(self, file:UploadFile):

        fileId= str(uuid.uuid4())

        content = await file.read()
        filename = f"{fileId}.apk"

        with open(os.path.join(self.APK_DIR, filename), "wb") as fp:
            fp.write(content)  

        fileMeta = {"filename":filename, "fileId":fileId}
        self.UploadFileMetaRepo.addUploadFileMeta(fileId, fileMeta)

        return {"filename": filename, "uuid": fileId}
    
    async def deleteApk(self, fileId:str):

        filename = f"{fileId}.apk"

        if not self.UploadFileMetaRepo.removeUploadFileMeta(fileId):
            return {"isError": "True", "errorMessage": "삭제하려는 파일이 존재하지 않습니다."}
        
        os.remove(os.path.join(self.APK_DIR, filename))

        return {"filename": filename, "uuid": fileId, "isError": "False"}