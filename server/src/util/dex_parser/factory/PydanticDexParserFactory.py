from src.util.dex_parser.DexParser import DexParser
from src.util.dex_parser.factory.DexParserFactory import DexParserFactory
from src.util.dex_parser.PydanticDexParser import PydanticDexParser


class PydanticDexParserFactory(DexParserFactory):
    def createDexparser(self) -> DexParser:
        return PydanticDexParser()
