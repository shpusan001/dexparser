from abc import *
from src.util.DexParser.DexParser import DexParser


class DexParserFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def createDexparser(self) -> DexParser:
        pass
