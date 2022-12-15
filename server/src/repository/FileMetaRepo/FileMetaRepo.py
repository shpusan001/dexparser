from abc import *


class FileMetaRepo(metaclass=ABCMeta):

    @abstractclassmethod
    def createFileMeta(self, fileId: str, meta: dict) -> bool:
        pass

    @abstractclassmethod
    def deleteFileMeta(self, fileId: str) -> bool:
        pass

    @abstractclassmethod
    def readFileMetaes(self) -> list:
        pass

    @abstractclassmethod
    def readFileMeta(self, fileId: str) -> str:
        pass
