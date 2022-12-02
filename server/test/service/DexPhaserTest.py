import pprint
import unittest
import os
import sys
import time
sys.path.append('./')

from src.service.DexParser.DexParser import *


class TestInit(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.stime = 0
        self.etime = 0

    def setUp(self) -> None:
        self.stime = time.time()
        return super().setUp()

    def tearDown(self) -> None:
        self.etime=time.time()
        print("Time:", self.etime - self.stime)
        return super().tearDown()


# class DexParserTest_getHeader(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getHeader()



# class DexParserTest_getStringFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getStringFull()


# class DexParserTest_getTypeFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getTypeFull()


# class DexParserTest_getProtoIds(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getProtoIds()

# class DexParserTest_getProtoFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getProtoFull()

       

# class DexParserTest_getFieldFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getFieldFull()


# class DexParserTest_getMethodIds(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getMethodIds()


# class DexParserTest_getMethodFull(TestInit):
#     def test_runs(self):
#         dexPaser = DexPaser()
#         dexPaser.setFile("./src/res/", "classes.dex")
#         res = dexPaser.getMethodFull()
#         pprint(res)

class DexParserTest_getClassFull(TestInit):
    def test_runs(self):
        dexPaser = DexPaser()
        dexPaser.setFile("./src/res/", "classes.dex")
        res = dexPaser.getClassFull()

        

if __name__ == '__main__':
    unittest.main()
