import sys
import os
sys.path.append('.')
import unittest
from src_test.test_init.DefaultTestInit import TestInit
from src.util.dex_parser.PydanticDexParser import PydanticDexParser
from src.util.HashDigester import HashDigester
import pprint

class PydanticDexParserTest(TestInit):

    def test_getParsedData(self):
        pydanticDexParser = PydanticDexParser()
        print(os.getcwd())
        pydanticDexParser.setFileFullPath("./src_test/res/classes.dex")
        
        tempFilePath = "./src_test/res/temp2.txt"

        with open(tempFilePath, mode="w") as fp:
            pprint.pprint(pydanticDexParser.getParsedData(), stream=fp)

        sha1 = HashDigester().sha1ForLageFile(tempFilePath)
        
        self.assertEqual(sha1, "178d7082f28638cd62f904976b770ba269b1ff61")

        os.remove(tempFilePath)
        

if __name__ == '__main__':
    unittest.main()   