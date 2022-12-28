from fastapi import APIRouter, Depends
from src.dto.ProgressDto import ProgressDto

from src.service.DexService import DexService


class ParsingRouter():

    dexService = DexService()

    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route("/parsing", self.parse, methods=["GET"])
        self.router.add_api_route(
            "/conv/hex2smali", self.hex2smali, methods=["POST"])
        self.router.add_api_route(
            "/progress", self.getProgress, methods=["GET"])

    def parse(self, res: dict = Depends(dexService.parseDex)):
        return res

    def hex2smali(self, res: dict = Depends(dexService.convertHex2Smali)):
        return res

    def getProgress(self, res: ProgressDto = Depends(dexService.getProgress)):
        return res
