from src.util.Singleton import Singleton
from src.util.DexParser.factory.DexParserFactory import DexParserFactory
from src.util.DexParser.factory.DictDexParserFactory import DictDexParserFactory
from src.util.DexParser.factory.PydanticDexParserFactory import PydanticDexParserFactory


class UtilContainer(Singleton):

    def __init__(self) -> None:
        pass

    def getDexParserFactory(self) -> DexParserFactory:
        return DictDexParserFactory()
