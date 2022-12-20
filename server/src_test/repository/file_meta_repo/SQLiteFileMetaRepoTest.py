import unittest
import sys
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.dto.FileMetaRepoDtos import FileMeta
from src.repository.file_meta_repo.SQLiteMetaRepo import SQLiteMetaRepo



class SQLiteFileMetaRepoTest(TestInit):
    sqliteMetaRepo = SQLiteMetaRepo()
    def test_createFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.sqliteMetaRepo.createFileMeta(fileId, fileMetaA)

        fileMetaB = self.sqliteMetaRepo.readFileMeta(fileId)

        self.assertEqual(fileMetaA.json(), fileMetaB.json())
        self.sqliteMetaRepo.deleteFileMeta(fileId)

    def test_deleteFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.sqliteMetaRepo.createFileMeta(fileId, fileMetaA)
        self.sqliteMetaRepo.deleteFileMeta(fileId)
        fileMetaB = self.sqliteMetaRepo.readFileMeta(fileId)
        self.assertEqual(fileMetaB, None)
        
    def test_readFileMeta(self):
        fileId = "123"
        data = {"fileName": "File.apk",
                "fileId": fileId, "sha1": "fake_sha1"}
        fileMetaA = FileMeta(**data)
        self.sqliteMetaRepo.createFileMeta(fileId, fileMetaA)

        fileMetaB = self.sqliteMetaRepo.readFileMeta(fileId)

        self.assertEqual(fileMetaA.json(), fileMetaB.json())
        self.sqliteMetaRepo.deleteFileMeta(fileId)
        
        

if __name__ == '__main__':
    unittest.main()   