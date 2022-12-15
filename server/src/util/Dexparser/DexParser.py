from abc import *


class DexParser(metaclass=ABCMeta):

    @abstractclassmethod
    def setFileFullPath(self, path: str) -> None:
        pass

    @abstractclassmethod
    def setFile(self, dirpath: str, filename: str) -> None:
        pass

    @abstractclassmethod
    def getHeader(self) -> dict:
        pass

    @abstractclassmethod
    def getParsedData(self) -> dict:
        pass
