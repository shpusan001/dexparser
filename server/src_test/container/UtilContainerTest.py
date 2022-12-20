import unittest
import sys
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.container.UtilContainer import UtilContainer


class UtilContainerTest(TestInit):
    def test_newUtilContainer(self):
        utilContainerA = UtilContainer()
        utilContainerB = UtilContainer()
        res = utilContainerA == utilContainerB
        self.assertEquals(res, True)

    def test_getDexParserFactory(self):
        dexParserFactoryA = UtilContainer().getDexParserFactory()
        dexParserFactoryB = UtilContainer().getDexParserFactory()
        res = dexParserFactoryA == dexParserFactoryB
        self.assertEquals(res, True)
        

if __name__ == '__main__':
    unittest.main()