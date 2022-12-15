from fastapi import APIRouter, Depends
from src.dto.FileManagerServiceDtos import *

from src.service.FileManageService import FileManageService

router = APIRouter()

fileManageService = FileManageService()


@router.post("/apk")
async def uploadApk(res: UploadApkRes = Depends(fileManageService.uploadApk)):
    return res


@router.delete("/apk")
async def deleteApk(res: DeleteApkRes = Depends(fileManageService.deleteApk)):
    return res


@router.get("/apk")
async def getApks(res: dict = Depends(fileManageService.getApks)):
    return res
