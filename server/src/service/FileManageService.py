from fastapi import UploadFile
import uuid
import os

from src.container.RepoContainer import RepoContainer
from src.util.Singleton import Singleton
from src.util.HashDigester import HashDigester


class FileManageService(Singleton):

    def __init__(self) -> None:
        self.fileMetaRepo = RepoContainer().getFileMetaRepo()
        self.hashDigester = HashDigester()

        self.WORK_DIR = "./work"
        self.APK_DIR = self.WORK_DIR + "/apk"

        try:
            if not os.path.isdir(self.WORK_DIR):
                os.mkdir(self.WORK_DIR)

            if not os.path.isdir(self.APK_DIR):
                os.mkdir(self.APK_DIR)
        except:
            pass

        if not os.path.isdir(self.APK_DIR):
            os.mkdir("./apk")

    async def uploadApk(self, file: UploadFile) -> dict:

        fileId = str(uuid.uuid4())

        content = await file.read()
        filename = f"{fileId}.apk"

        fileWritePath = os.path.join(self.APK_DIR, filename)
        with open(fileWritePath, "wb") as fp:
            fp.write(content)

        fileHash = self.hashDigester.sha1ForLageFile(fileWritePath)

        fileMeta = {"fileName": file.filename,
                    "fileId": fileId, "sha1": fileHash}
        self.fileMetaRepo.createFileMeta(fileId, fileMeta)

        return {"fileName": filename, "uuid": fileId}

    async def deleteApk(self, fileId: str) -> dict:

        filename = f"{fileId}.apk"

        if not self.fileMetaRepo.deleteFileMeta(fileId):
            return {"isError": "True", "errorMessage": "삭제하려는 파일이 존재하지 않습니다."}

        os.remove(os.path.join(self.APK_DIR, filename))

        return {"fileName": filename, "uuid": fileId, "isError": "False"}

    async def getApks(self) -> dict:
        files = self.fileMetaRepo.readFileMetaes()
        res = {"files": files}
        return res
