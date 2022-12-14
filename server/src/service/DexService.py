import glob
import shutil
import os
from struct import unpack
import zipfile
from pydantic import BaseModel
from typing import Optional
from src.dto.ProgressDto import ProgressDto
from src.util.Singleton import Singleton
from src.util.DexParser import DexPaser
from src.util.DexDecompiler import DexDecompiler
from src.repository.UploadFileMetaRepo import UploadFileMetaRepo
from src.repository.ProgressRepo import ProgressRepo


class DexService(Singleton):
    def __init__(self) -> None:
        self.uploadFileMetaRepo = UploadFileMetaRepo()
        self.progressRepo = ProgressRepo()

        self.SAVE_DIR = "./apk"
        self.WORK_DIR = "./work"
        self.DEX_DIR = "./dex"

        if not os.path.isdir(self.SAVE_DIR):
            os.mkdir("./apk")

        if not os.path.isdir(self.WORK_DIR):
            os.mkdir("./work")

        if not os.path.isdir(self.DEX_DIR):
            os.mkdir("./dex")

    async def parseDex(self, fileId: str, reqKey: str) -> dict:
        # apk를 작업 디렉토리로 복사
        shutil.copy(os.path.join(self.SAVE_DIR, fileId+".apk"),
                    os.path.join(self.WORK_DIR, fileId+".apk"))
        apkFile = zipfile.ZipFile(os.path.join(self.WORK_DIR, fileId+".apk"))
        apkFile.extractall(os.path.join(self.WORK_DIR))
        apkFile.close()

        # 읽기 권한이 없는 폴더 삭제
        # removeList = ["/r", "/kotlin", "/META-INF", "/lib",
        #               "/assets", "/res", "okhttp3", "dmaplibres"]
        # for rm in removeList:
        #     if os.path.isdir(self.WORK_DIR + rm):
        #         shutil.rmtree(self.WORK_DIR + rm)

        # 디렉토리들 모두 삭제
        for file in os.scandir(self.WORK_DIR):
            if file.is_dir():
                shutil.rmtree(file.path)

        # dex파일만 뽑음
        fileList = os.listdir(self.WORK_DIR)
        dexList = [file for file in fileList if file.endswith(".dex")]

        # dex파일을 작업 디렉토리에서 덱스디렉토리로 복사
        for dex in dexList:
            shutil.copy(os.path.join(self.WORK_DIR, dex),
                        os.path.join(self.DEX_DIR, dex))

        # 모든 클래스 개수 파악 (프로그래스 바 구현에 사용됨)
        totalSize = 0
        for file in os.scandir(self.DEX_DIR):
            dexParser = DexPaser()
            dexParser.setFileFullPath(file.path)
            header = dexParser.getHeader()
            classDefSize = unpack("<I", header["class_defs_size"])[0]
            totalSize += classDefSize

        self.progressRepo.addProgress(reqKey, totalSize)

        # 모든 덱스 파싱
        parsingResults = list()
        for file in os.scandir(self.DEX_DIR):
            dexParser = DexPaser()
            dexParser.setFileFullPath(file.path)
            parsingResult = dexParser.getClassFull(reqKey=reqKey)
            parsingResults.append(
                {"fileName": file.name, "data": parsingResult})

        fileName = self.uploadFileMetaRepo.getFileName(fileId)

        res = {"fileName": fileName, "fileId": fileId, "results": parsingResults}

        self.__deleteAllFiles(self.WORK_DIR)
        self.__deleteAllFiles(self.DEX_DIR)

        self.progressRepo.removeProgress(reqKey)

        return res

    async def getProgress(self, reqKey: str, nowValue: int, maxValue: int) -> ProgressDto:
        currentProgress = self.progressRepo.readProgress(reqKey)
        if currentProgress != None:
            return currentProgress
        else:
            data = {"nowValue": nowValue, "maxValue": maxValue}
            progress = ProgressDto(**data)
            return progress

    class Hex(BaseModel):
        hexcode: str

    def convertHex2Smali(self, hexcode: Hex) -> dict:
        bytecode = bytes.fromhex(hexcode.hexcode)
        dexDecompiler = DexDecompiler()
        dexDecompiler.load_bytearray(bytecode)

        res = {"smali": dexDecompiler.disassemble()}
        return res

    def __deleteAllFiles(self, filePath: str) -> None:
        if os.path.exists(filePath):
            for file in os.scandir(filePath):
                os.remove(file.path)
