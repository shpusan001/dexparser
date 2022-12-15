from abc import *
from src.dto.DexparserDtoes import *


class DexParser(metaclass=ABCMeta):

    @abstractclassmethod
    def setReqKey(self, reqKey: str):
        pass

    @abstractclassmethod
    def setFileFullPath(self, path: str) -> None:
        pass

    @abstractclassmethod
    def setFile(self, dirpath: str, filename: str) -> None:
        pass

    @abstractclassmethod
    def getHeader(self) -> Header:
        pass

    @abstractclassmethod
    def getParsedData(self) -> dict:
        pass
