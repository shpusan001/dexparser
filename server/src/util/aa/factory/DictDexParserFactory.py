from src.util.DexParser.DexParser import DexParser
from src.util.DexParser.factory.DexParserFactory import DexParserFactory
from src.util.DexParser.DictDexParser import DictDexParser


class DictDexParserFactory(DexParserFactory):
    def createDexparser(self) -> DexParser:
        return DictDexParser()
