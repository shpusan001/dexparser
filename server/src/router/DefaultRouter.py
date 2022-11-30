import sys
sys.path.append('../')
from fastapi import APIRouter


from src.service.DexParser.DexParser import DexPaser


router = APIRouter()


@router.get("/")
async def home():
    return {"msg": "hello world"}


@router.get("/parse")
async def parse():
    DexPaser()
    return {}
