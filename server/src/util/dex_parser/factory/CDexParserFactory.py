from src.util.dex_parser.DexParser import DexParser
from src.util.dex_parser.CDexParser import CDexParser
from src.util.dex_parser.factory.DexParserFactory import DexParserFactory


class CDexParserFactory(DexParserFactory):
    def createDexparser(self) -> DexParser:
        return CDexParser()
