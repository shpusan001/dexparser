from typing import List, Optional
from src.dto.FileMetaRepoDtos import FileMeta
from src.repository.FileMetaRepo.FileMetaRepo import FileMetaRepo
import pickle
import os


class DictFileMetaRepo(FileMetaRepo):

    def __init__(self) -> None:
        self.uploadFiles = dict()

        self.WORK_DIR = "./work"
        self.DB_DIR = self.WORK_DIR + "/db"
        self.DB_PATH = self.DB_DIR + "/file.dict"

        try:
            if not os.path.isdir(self.WORK_DIR):
                os.mkdir(self.WORK_DIR)

            if not os.path.isdir(self.DB_DIR):
                os.mkdir(self.DB_DIR)

            if not os.path.isfile(self.DB_PATH):
                with open(self.DB_PATH, 'wb') as f:
                    pickle.dump({}, f)
                    pass
        except:
            pass

        self.__loadUploadFiles()

    def createFileMeta(self, fileId: str, meta: FileMeta) -> bool:
        self.__syncDatabase()

        self.uploadFiles[fileId] = meta

        self.__syncDatabase()
        return True

    def deleteFileMeta(self, fileId: str) -> bool:
        self.__syncDatabase()
        if fileId in self.uploadFiles:
            del self.uploadFiles[fileId]
            self.__saveUploadFiles()
            self.__syncDatabase()
            return True
        else:
            self.__syncDatabase()
            return False

    def readFileMetaes(self) -> List[FileMeta]:
        self.__syncDatabase()

        res = list()

        files = self.uploadFiles.items()
        for value in files:
            fileMeta = value[1]
            res.append(fileMeta)

        self.__syncDatabase()
        return res

    def readFileMeta(self, fileId: str) -> Optional[FileMeta]:
        self.__syncDatabase()
        try:
            fileMeta = self.uploadFiles[fileId]
        except:
            return None

        self.__syncDatabase()
        return fileMeta

    def __syncDatabase(self):
        self.__saveUploadFiles()
        self.__loadUploadFiles()

    def __saveUploadFiles(self):
        with open(self.DB_PATH, 'wb') as fp:
            pickle.dump(self.uploadFiles, fp)

    def __loadUploadFiles(self):
        with open(self.DB_PATH, 'rb') as fp:
            self.uploadFiles = pickle.load(fp)
