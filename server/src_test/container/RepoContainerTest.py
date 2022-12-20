import sys

sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.container.RepoContainer import RepoContainer



class RepoContainerTest(TestInit):
    def test_newRepoContainer(self):
        repoContainerA = RepoContainer()
        repoContainerB = RepoContainer()
        res = repoContainerA == repoContainerB
        self.assertEqual(res, True)

    def test_getFileMetaRepo(self):
        fileMetaRepoA = RepoContainer().getFileMetaRepo()
        fileMetaRepoB = RepoContainer().getFileMetaRepo()
        res = fileMetaRepoA == fileMetaRepoB
        self.assertEqual(res, True)

    def test_getProgressRepo(self):
        progressRepoA = RepoContainer().getProgressRepo()
        progressRepoB = RepoContainer().getProgressRepo()
        res = progressRepoA == progressRepoB
        self.assertEqual(res, True)
        

if __name__ == '__main__':
    unittest.main()
