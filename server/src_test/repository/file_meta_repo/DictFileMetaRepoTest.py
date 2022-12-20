import unittest
import sys
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.dto.FileMetaRepoDtos import FileMeta
from src.repository.file_meta_repo.DictFileMetaRepo import DictFileMetaRepo



class DictFileMetaRepoTest(TestInit):
    dictFileMetaRepo = DictFileMetaRepo()
    def test_createFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.dictFileMetaRepo.createFileMeta(fileId, fileMetaA)

        fileMetaB = self.dictFileMetaRepo.readFileMeta(fileId)

        self.assertEqual(fileMetaA.json(), fileMetaB.json())
        self.dictFileMetaRepo.deleteFileMeta(fileId)

    def test_deleteFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.dictFileMetaRepo.createFileMeta(fileId, fileMetaA)
        self.dictFileMetaRepo.deleteFileMeta(fileId)
        fileMetaB = self.dictFileMetaRepo.readFileMeta(fileId)
        self.assertEqual(fileMetaB, None)
        
    def test_readFileMetaes(self):
        fileId1 = "123"
        data1 = {"fileName": "File.apk",
                "fileId": fileId1, "sha1": "fake_sha1"}
        fileId2 = "456"
        data2 = {"fileName": "File.apk",
                "fileId": fileId2, "sha1": "fake_sha1"}
        fileId3 = "789"
        data3 = {"fileName": "File.apk",
                "fileId": fileId3, "sha1": "fake_sha1"}

        fileMeta1 = FileMeta(**data1)
        fileMeta2 = FileMeta(**data2)
        fileMeta3 = FileMeta(**data3)

        self.dictFileMetaRepo.createFileMeta(fileId1, fileMeta1)
        self.dictFileMetaRepo.createFileMeta(fileId2, fileMeta2)
        self.dictFileMetaRepo.createFileMeta(fileId3, fileMeta3)

        readedFileMeta1 = self.dictFileMetaRepo.readFileMeta(fileId1)
        readedFileMeta2 = self.dictFileMetaRepo.readFileMeta(fileId2)
        readedFileMeta3 = self.dictFileMetaRepo.readFileMeta(fileId3)

        fileMetaList = self.dictFileMetaRepo.readFileMetaes()

        self.assertEqual(readedFileMeta1, fileMetaList[0])
        self.assertEqual(readedFileMeta2, fileMetaList[1])
        self.assertEqual(readedFileMeta3, fileMetaList[2])
        
        self.dictFileMetaRepo.deleteFileMeta(fileId1)
        self.dictFileMetaRepo.deleteFileMeta(fileId2)
        self.dictFileMetaRepo.deleteFileMeta(fileId3)
        
    def test_readFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.dictFileMetaRepo.createFileMeta(fileId, fileMetaA)

        fileMetaB = self.dictFileMetaRepo.readFileMeta(fileId)

        self.assertEqual(fileMetaA.json(), fileMetaB.json())
        self.dictFileMetaRepo.deleteFileMeta(fileId)
        
        

if __name__ == '__main__':
    unittest.main()   