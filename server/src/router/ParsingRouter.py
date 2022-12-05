import sys
from fastapi import APIRouter


from src.util.DexParser import DexPaser


router = APIRouter()


@router.get("/parsing")
async def parse(fileId:str):

    return {"msg": "hello world"}
