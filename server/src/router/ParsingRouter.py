import sys
from fastapi import APIRouter


from src.service.DexParser.DexParser import DexPaser


router = APIRouter()


@router.get("/")
async def home():
    return {"msg": "hello world"}
