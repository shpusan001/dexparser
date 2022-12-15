from abc import *
from typing import List, Optional

from src.dto.FileMetaRepoDtos import FileMeta


class FileMetaRepo(metaclass=ABCMeta):

    @abstractclassmethod
    def createFileMeta(self, fileId: str, meta: FileMeta) -> bool:
        pass

    @abstractclassmethod
    def deleteFileMeta(self, fileId: str) -> bool:
        pass

    @abstractclassmethod
    def readFileMetaes(self) -> List[FileMeta]:
        pass

    @abstractclassmethod
    def readFileMeta(self, fileId: str) -> Optional[FileMeta]:
        pass
