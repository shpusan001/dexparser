from src.util.Singleton import Singleton
import os
import pickle

class UploadFileMetaRepo(Singleton):

    def __init__(self) -> None:
        self.uploadFiles = dict()
        self.DIR = "./uploadFiles.dict"
        try:
            with open(self.DIR,'rb') as fp:
                self.uploadFiles = pickle.load(fp)
        except:
            self.__saveUploadFiles()


    def addUploadFileMeta(self, fileId:str, meta:dict)->bool:
        self.uploadFiles[fileId] = meta
        self.__saveUploadFiles()
        return True

    def removeUploadFileMeta(self, fileId:str)->bool:
        if fileId in self.uploadFiles:
            del self.uploadFiles[fileId]
            self.__saveUploadFiles()
            return True
        return False


    def __saveUploadFiles(self):
        with open(self.DIR,'wb') as fp:
            pickle.dump(self.uploadFiles,fp)
