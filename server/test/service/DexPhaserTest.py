import pprint
import unittest
import os
import sys
sys.path.append('./')

from src.service.DexParser.DexParser import *


class TestInit(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()


class DexParserTest_getHeader(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getHeader()

        pprint.pprint(res)

        # self.assertDictEqual(res, {})


class DexParserTest_getStringFull(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getStringFull()


        # self.assertDictEqual(res, {})

class DexParserTest_getTypeFull(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getTypeFull()

class DexParserTest_getProtoIds(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getProtoIds()

class DexParserTest_getProtoFull(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getProtoFull()

        # self.assertDictEqual(res, {})
if __name__ == '__main__':
    unittest.main()
