from abc import *
from src.util.dex_parser.DexParser import DexParser


class DexParserFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def createDexparser(self) -> DexParser:
        pass
