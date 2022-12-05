from fastapi import UploadFile
import uuid
import os
import pickle

from src.repository.UploadFileMetaRepo import UploadFileMetaRepo
from src.util.Singleton import Singleton
from src.util.HashDigester import HashDigester

class FileManageService(Singleton):

    def __init__(self) -> None:
        self.APK_DIR = "./apk"
        self.uploadFileMetaRepo = UploadFileMetaRepo()
        self.hashDigester = HashDigester()

        if not os.path.isdir(self.APK_DIR):
            os.mkdir("./apk")


    async def uploadApk(self, file:UploadFile)->dict:

        fileId= str(uuid.uuid4())

        content = await file.read()
        filename = f"{fileId}.apk"

        fileWritePath = os.path.join(self.APK_DIR, filename)
        with open(fileWritePath, "wb") as fp:
            fp.write(content)  

        fileHash = self.hashDigester.sha1ForLageFile(fileWritePath)

        fileMeta = {"fileName":file.filename, "fileId":fileId, "sha1": fileHash}
        self.uploadFileMetaRepo.addUploadFileMeta(fileId, fileMeta)

        return {"fileName": filename, "uuid": fileId}
    
    async def deleteApk(self, fileId:str)->dict:

        filename = f"{fileId}.apk"

        if not self.uploadFileMetaRepo.removeUploadFileMeta(fileId):
            return {"isError": "True", "errorMessage": "삭제하려는 파일이 존재하지 않습니다."}
        
        os.remove(os.path.join(self.APK_DIR, filename))

        return {"fileName": filename, "uuid": fileId, "isError": "False"}

    async def getApks(self)->dict:
        files = self.uploadFileMetaRepo.getFiles()
        res = {"files": files}
        return res

