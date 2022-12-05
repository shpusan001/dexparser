import glob
import shutil
import os
import zipfile

from src.util.Singleton import Singleton
from src.util.DexParser import DexPaser
from src.util.DexDecompiler import DexDecompiler
from src.repository.UploadFileMetaRepo import UploadFileMetaRepo


class DexService(Singleton):
    def __init__(self) -> None:
        self.uploadFileMetaRepo = UploadFileMetaRepo()

        self.SAVE_DIR = "./apk"
        self.WORK_DIR = "./work"
        self.DEX_DIR = "./dex"

        if not os.path.isdir(self.SAVE_DIR):
            os.mkdir("./apk")

        if not os.path.isdir(self.WORK_DIR):
            os.mkdir("./work")

        if not os.path.isdir(self.DEX_DIR):
            os.mkdir("./dex")
    
    async def parseDex(self, fileId:str)->dict:
        #apk를 작업 디렉토리로 복사
        shutil.copy(os.path.join(self.SAVE_DIR, fileId+".apk"), os.path.join(self.WORK_DIR, fileId+".apk"))
        apkFile = zipfile.ZipFile(os.path.join(self.WORK_DIR, fileId+".apk"))
        apkFile.extractall(os.path.join(self.WORK_DIR))
        apkFile.close()

        #읽기 권한이 없는 폴더 삭제
        shutil.rmtree(self.WORK_DIR + "/r")
        shutil.rmtree(self.WORK_DIR + "/kotlin")
        shutil.rmtree(self.WORK_DIR + "/META-INF")
        shutil.rmtree(self.WORK_DIR + "/lib")
        shutil.rmtree(self.WORK_DIR + "/assets")
        
        #dex파일만 뽑음
        fileList = os.listdir(self.WORK_DIR)
        dexList = [file for file in fileList if file.endswith(".dex")]
        
        #dex파일을 작업 디렉토리에서 덱스디렉토리로 복사
        for dex in dexList:
            shutil.copy(os.path.join(self.WORK_DIR, dex), os.path.join(self.DEX_DIR, dex))

        #모든 덱스 파싱
        parsingResults = list()
        for file in os.scandir(self.DEX_DIR):
            dexParser = DexPaser()
            dexParser.setFileFullPath(file.path)
            parsingResult = dexParser.getClassFull()
            parsingResults.append({"fileName":file.name, "data":parsingResult})
        
        fileName = self.uploadFileMetaRepo.getFileName(fileId)

        res = {"fileName": fileName, "results" : parsingResults}

        self.__deleteAllFiles(self.WORK_DIR)
        self.__deleteAllFiles(self.DEX_DIR)

        return res
    
    def convertHex2Smali(self, hex:str)->dict:
        bytecode = bytes.fromhex(hex)
        dexDecompiler = DexDecompiler()
        dexDecompiler.load_bytearray(bytecode)

        res = {"smali": dexDecompiler.disassemble()}
        return res


    def __deleteAllFiles(self, filePath:str)->None:
        if os.path.exists(filePath):
            for file in os.scandir(filePath):
                os.remove(file.path)


        
