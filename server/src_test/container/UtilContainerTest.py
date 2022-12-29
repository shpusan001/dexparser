from src.container.UtilContainer import UtilContainer
from src_test.test_init.DefaultTestInit import TestInit
import unittest
import sys
sys.path.append('.')


class UtilContainerTest(TestInit):
    def test_newUtilContainer(self):
        utilContainerA = UtilContainer()
        utilContainerB = UtilContainer()
        res = utilContainerA == utilContainerB
        self.assertEqual(res, True)

    def test_getDexParserFactory(self):
        dexParserFactoryA = UtilContainer().getDexParserFactory()
        dexParserFactoryB = UtilContainer().getDexParserFactory()
        res = dexParserFactoryA == dexParserFactoryB
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
