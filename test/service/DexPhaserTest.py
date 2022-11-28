import sys
sys.path.append('.')
import os
import unittest
import src.service.DexParser as DexPaser

class TestInit(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

class DexPaserTest(TestInit):
    def test_runs(self):
        dexPaser = DexPaser.DexPaser()
        dexPaser.setFile(os.getcwd()+"\\src\\res\\", "classes.dex")
        res = dexPaser.parseHeader()
        
        self.assertDictEqual(res, {})

if __name__ == '__main__':
    unittest.main()