import unittest
import sys
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.dto.FileMetaRepoDtos import FileMeta
from src.repository.progress_repo.SQLiteProgressRepo import SQLiteProgressRepo
from src.dto.ProgressDto import ProgressDto



class SQLiteFileMetaRepoTest(TestInit):
    sqliteProgressRepo = SQLiteProgressRepo()
    def test_createProgress(self):
        reqKey = 0
        maxValue=100
        self.sqliteProgressRepo.createProgress(reqKey, maxValue)
        progress:ProgressDto = self.sqliteProgressRepo.readProgress(reqKey)
        self.assertEqual(progress.maxValue, maxValue)
        self.assertEqual(progress.nowValue, 0)
        self.sqliteProgressRepo.deleteProgress(reqKey)

    def test_readProgress(self):
        reqKey = 0
        maxValue=100
        self.sqliteProgressRepo.createProgress(reqKey, maxValue)
        progress:ProgressDto = self.sqliteProgressRepo.readProgress(reqKey)
        self.assertEqual(progress.maxValue, maxValue)
        self.assertEqual(progress.nowValue, 0)
        self.sqliteProgressRepo.deleteProgress(reqKey)

    def test_updateProgress(self):
        reqKey = 0
        maxValue=100
        self.sqliteProgressRepo.createProgress(reqKey, maxValue)

        self.sqliteProgressRepo.updateProgress(reqKey,3)
        self.sqliteProgressRepo.updateProgress(reqKey,2)
        self.sqliteProgressRepo.updateProgress(reqKey)

        progress:ProgressDto = self.sqliteProgressRepo.readProgress(reqKey)

        self.assertEqual(progress.maxValue, maxValue)
        self.assertEqual(progress.nowValue, 6)

        self.sqliteProgressRepo.deleteProgress(reqKey)
        
    def test_deleteProgress(self):
        reqKey = 0
        maxValue=100
        self.sqliteProgressRepo.createProgress(reqKey, maxValue)

        progress:ProgressDto = self.sqliteProgressRepo.readProgress(reqKey)

        self.sqliteProgressRepo.deleteProgress(reqKey)

        progress:ProgressDto = self.sqliteProgressRepo.readProgress(reqKey)
        
        self.assertEqual(progress, None)

if __name__ == '__main__':
    unittest.main()   