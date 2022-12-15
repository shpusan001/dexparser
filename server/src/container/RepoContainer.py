from src.util.Singleton import Singleton
from src.repository.FileMetaRepo.FileMetaRepo import FileMetaRepo
from src.repository.FileMetaRepo.DictFileMetaRepo import DictFileMetaRepo
from src.repository.FileMetaRepo.SQLiteMetaRepo import SQLiteMetaRepo
from src.repository.ProgressRepo.ProgressRepo import ProgressRepo
from src.repository.ProgressRepo.SQLiteProgressRepo import SQLiteProgressRepo


class RepoContainer(Singleton):

    def __init__(self) -> None:
        self.__fileMetaRepo: FileMetaRepo = None
        self.__progressRepo: ProgressRepo = None

    def getFileMetaRepo(self) -> FileMetaRepo:
        if self.__fileMetaRepo == None:
            self.__fileMetaRepo = SQLiteMetaRepo()
        return self.__fileMetaRepo

    def getProgressRepo(self) -> ProgressRepo:
        if self.__progressRepo == None:
            self.__progressRepo = SQLiteProgressRepo()
        return self.__progressRepo
