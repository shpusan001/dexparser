from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"msg": "hello world"}

@router.get("/pharse")
async def parse():
    
    return {}