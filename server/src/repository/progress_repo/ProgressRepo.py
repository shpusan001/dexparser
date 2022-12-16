from abc import *

from src.dto.ProgressDto import ProgressDto


class ProgressRepo(metaclass=ABCMeta):
    @abstractclassmethod
    def createProgress(self, reqKey: str, maxValue: int) -> None:
        pass

    @abstractclassmethod
    def readProgress(self, reqKey: str) -> ProgressDto:
        pass

    @abstractclassmethod
    def updateProgress(self, reqKey: str, value: int = 1) -> None:
        pass

    @abstractclassmethod
    def deleteProgress(self, reqKey: str) -> None:
        pass
