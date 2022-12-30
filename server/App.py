from src.router.ApkRouter import ApkRouter
from src.router.ParsingRouter import ParsingRouter
from src.router.UtilRouter import UtilRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import json
sys.path.append('.')


# python-multipart, construct 2.5.3, fastapi

app = FastAPI()

app.include_router(ParsingRouter().router)
app.include_router(ApkRouter().router)
app.include_router(UtilRouter().router)

fp = open("./setting.json", "r")
setting = json.load(fp)
fp.close()

origins = setting["cors"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
