from src.router.ApkRouter import ApkRouter
from src.router.ParsingRouter import ParsingRouter

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append('.')


# python-multipart, construct 2.5.3, fastapi

app = FastAPI()

app.include_router(ParsingRouter().router)
app.include_router(ApkRouter().router)

origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
