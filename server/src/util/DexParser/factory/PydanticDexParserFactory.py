from src.util.DexParser.DexParser import DexParser
from src.util.DexParser.factory.DexParserFactory import DexParserFactory
from src.util.DexParser.PydanticDexParser import PydanticDexParser


class PydanticDexParserFactory(DexParserFactory):
    def createDexparser(self) -> DexParser:
        return PydanticDexParser()
