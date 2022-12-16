from src.util.dex_parser.DexParser import DexParser
from src.util.dex_parser.factory.DexParserFactory import DexParserFactory
from src.util.dex_parser.DictDexParser import DictDexParser


class DictDexParserFactory(DexParserFactory):
    def createDexparser(self) -> DexParser:
        return DictDexParser()
