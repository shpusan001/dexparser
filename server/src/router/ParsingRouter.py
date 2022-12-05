import sys
from fastapi import APIRouter, Depends


from src.service.DexService import DexService


router = APIRouter()


dexService = DexService()


@router.get("/parsing")
async def parse(res:dict = Depends(dexService.parseDex)):
    return res

@router.post("/conv/hex2smali")
async def hex2smali(res:dict = Depends(dexService.convertHex2Smali)):
    return res
