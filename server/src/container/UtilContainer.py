from src.util.Singleton import Singleton
from src.util.dex_parser.factory.CDexParserFactory import CDexParserFactory
from src.util.dex_parser.factory.DexParserFactory import DexParserFactory
from src.util.dex_parser.factory.DictDexParserFactory import DictDexParserFactory
from src.util.dex_parser.factory.PydanticDexParserFactory import PydanticDexParserFactory


class UtilContainer(Singleton):
    __dexParserFactory: DexParserFactory = None

    def __init__(self) -> None:
        pass

    def getDexParserFactory(self) -> DexParserFactory:
        if self.__dexParserFactory == None:
            self.__dexParserFactory = CDexParserFactory()
        return self.__dexParserFactory
