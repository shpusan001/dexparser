import shutil
import os
import zipfile
from pydantic import BaseModel
from src.repository.FileMetaRepo.FileMetaRepo import FileMetaRepo
from src.repository.ProgressRepo.ProgressRepo import ProgressRepo
from src.dto.ProgressDto import ProgressDto
from src.util.Singleton import Singleton
from src.util.DexDecompiler import DexDecompiler
from src.container.RepoContainer import RepoContainer
from src.container.UtilContainer import UtilContainer
from src.util.DexParser.factory.DexParserFactory import DexParserFactory
from src.util.DexParser.DexParser import DexParser


class DexService(Singleton):
    def __init__(self) -> None:
        self.fileMetaRepo: FileMetaRepo = RepoContainer().getFileMetaRepo()
        self.progressRepo: ProgressRepo = RepoContainer().getProgressRepo()
        self.dexParserFactory: DexParserFactory = UtilContainer().getDexParserFactory()

        self.WORK_DIR: str = "./work"

        self.APK_DIR: str = self.WORK_DIR + "/apk"
        self.UNZIP_DIR: str = self.WORK_DIR + "/unzip"
        self.DEX_DIR: str = self.WORK_DIR + "/dex"

        try:
            if not os.path.isdir(self.WORK_DIR):
                os.mkdir(self.WORK_DIR)

            if not os.path.isdir(self.APK_DIR):
                os.mkdir(self.APK_DIR)

            if not os.path.isdir(self.UNZIP_DIR):
                os.mkdir(self.UNZIP_DIR)

            if not os.path.isdir(self.DEX_DIR):
                os.mkdir(self.DEX_DIR)
        except:
            pass

    async def parseDex(self, fileId: str, reqKey: str) -> dict:

        REQ_UNZIP_DIR = self.UNZIP_DIR+"/"+reqKey
        REQ_DEX_DIR = self.DEX_DIR+"/"+reqKey

        os.mkdir(REQ_UNZIP_DIR)
        os.mkdir(REQ_DEX_DIR)

        # apk를 작업 디렉토리로 복사
        shutil.copy(os.path.join(self.APK_DIR, fileId+".apk"),
                    os.path.join(REQ_UNZIP_DIR, fileId+".apk"))
        apkFile = zipfile.ZipFile(os.path.join(REQ_UNZIP_DIR, fileId+".apk"))
        apkFile.extractall(os.path.join(REQ_UNZIP_DIR))
        apkFile.close()

        # 디렉토리들 모두 삭제
        for file in os.scandir(REQ_UNZIP_DIR):
            if file.is_dir():
                shutil.rmtree(file.path)

        # dex파일만 뽑음
        fileList = os.listdir(REQ_UNZIP_DIR)
        dexList = [file for file in fileList if file.endswith(".dex")]

        # dex파일을 작업 디렉토리에서 덱스디렉토리로 복사
        for dex in dexList:
            shutil.copy(os.path.join(REQ_UNZIP_DIR, dex),
                        os.path.join(REQ_DEX_DIR, dex))

        # 모든 클래스 개수 파악 (프로그래스 바 구현에 사용됨)
        # 모든 프로토(proto) 개수 파악 (프로그래스 바 구현에 사용됨)
        totalSize = 0
        for file in os.scandir(REQ_DEX_DIR):
            dexParser: DexParser = self.dexParserFactory.createDexparser()
            dexParser.setReqKey(reqKey)
            dexParser.setFileFullPath(file.path)
            header = dexParser.getHeader()

            classDefSize = header.class_defs_size
            protoSize = header.proto_ids_size

            totalSize += classDefSize
            totalSize += protoSize

        self.progressRepo.createProgress(reqKey, totalSize)

        # 모든 덱스 파싱
        parsingResults = list()
        for file in os.scandir(REQ_DEX_DIR):
            dexParser: DexParser = self.dexParserFactory.createDexparser()
            dexParser.setReqKey(reqKey)
            dexParser.setFileFullPath(file.path)
            parsingResult = dexParser.getClassFull()
            parsingResults.append(
                {"fileName": file.name, "data": parsingResult})

        fileName = self.fileMetaRepo.readFileMeta(fileId).fileName

        res = {"fileName": fileName, "fileId": fileId, "results": parsingResults}

        shutil.rmtree(REQ_UNZIP_DIR)
        shutil.rmtree(REQ_DEX_DIR)

        self.progressRepo.deleteProgress(reqKey)

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

    def __getCleanDexFileName(self, name: str) -> str:
        splitPoint = name.rfind("-")
        return name[splitPoint+1:]
