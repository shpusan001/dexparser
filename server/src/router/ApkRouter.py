from fastapi import APIRouter, Depends
from src.dto.FileManagerServiceDtoes import *
from src.service.FileManageService import FileManageService


class ApkRouter():

    fileManageService = FileManageService()

    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route("/apk", self.uploadApk, methods=["POST"])
        self.router.add_api_route("/apk", self.deleteApk, methods=["DELETE"])
        self.router.add_api_route("/apk", self.getApks, methods=["GET"])

    def uploadApk(self, res: UploadApkRes = Depends(fileManageService.uploadApk)):
        return res

    def deleteApk(self, res: DeleteApkRes = Depends(fileManageService.deleteApk)):
        return res

    async def getApks(self, res: dict = Depends(fileManageService.getApks)):
        return res
