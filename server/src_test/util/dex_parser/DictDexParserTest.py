import sys
import os
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.util.dex_parser.DictDexParser import DictDexParser
from src.util.HashDigester import HashDigester
import pprint

class DictDexParserTest(TestInit):

    def test_getParsedData(self):
        dictDexParser = DictDexParser()
        print(os.getcwd())
        dictDexParser.setFileFullPath("./src_test/res/classes.dex")
        
        tempFilePath = "./src_test/res/temp1.txt"

        with open(tempFilePath, mode="w") as fp:
            pprint.pprint(dictDexParser.getParsedData(), stream=fp)

        sha1 = HashDigester().sha1ForLageFile(tempFilePath)
        
        self.assertEqual(sha1, "178d7082f28638cd62f904976b770ba269b1ff61")

        os.remove(tempFilePath)
        

if __name__ == '__main__':
    unittest.main()   