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
        except:
            pass

        try:
            with open(self.DB_PATH, 'rb') as fp:
                self.uploadFiles = pickle.load(fp)
        except:
            self.__saveUploadFiles()

    def createFileMeta(self, fileId: str, meta: dict) -> bool:
        self.uploadFiles[fileId] = meta
        self.__saveUploadFiles()
        return True

    def deleteFileMeta(self, fileId: str) -> bool:
        if fileId in self.uploadFiles:
            del self.uploadFiles[fileId]
            self.__saveUploadFiles()
            return True
        return False

    def readFileMetaes(self) -> list:
        self.__loadUploadFiles()

        res = list()

        files = self.uploadFiles.items()
        for value in files:
            res.append(value[1])
        return res

    def readFileMeta(self, fileId: str) -> dict:
        return self.uploadFiles[fileId]

    def __saveUploadFiles(self):
        with open(self.DB_PATH, 'wb') as fp:
            pickle.dump(self.uploadFiles, fp)

    def __loadUploadFiles(self):
        with open(self.DB_PATH, 'rb') as fp:
            self.uploadFiles = pickle.load(fp)
