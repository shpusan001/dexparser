import sys
from fastapi import APIRouter, Depends

from src.service.FileManageService import FileManageService

router = APIRouter()

fileManageService = FileManageService()

@router.post("/apk")
async def uploadApk(res:dict = Depends(fileManageService.uploadApk)):
    return res

@router.delete("/apk")
async def deleteApk(res:dict = Depends(fileManageService.deleteApk)):
    return res

@router.get("/apk")
async def getApks(res:dict = Depends(fileManageService.getApks)):
    return res