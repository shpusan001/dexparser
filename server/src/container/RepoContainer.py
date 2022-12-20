from src.util.Singleton import Singleton
from src.repository.file_meta_repo.FileMetaRepo import FileMetaRepo
from src.repository.file_meta_repo.DictFileMetaRepo import DictFileMetaRepo
from src.repository.file_meta_repo.SQLiteMetaRepo import SQLiteMetaRepo
from src.repository.progress_repo.ProgressRepo import ProgressRepo
from src.repository.progress_repo.SQLiteProgressRepo import SQLiteProgressRepo


class RepoContainer(Singleton):
    __fileMetaRepo: FileMetaRepo = None
    __progressRepo: ProgressRepo = None

    def __init__(self) -> None:
        pass
    
    def getFileMetaRepo(self) -> FileMetaRepo:
        if self.__fileMetaRepo == None:
            self.__fileMetaRepo = SQLiteMetaRepo()
        return self.__fileMetaRepo

    def getProgressRepo(self) -> ProgressRepo:
        if self.__progressRepo == None:
            self.__progressRepo = SQLiteProgressRepo()
        return self.__progressRepo
