import src.router.ApkRouter as ApkRouter
import src.router.ParsingRouter as ParsingRouter
import src.router.DefaultRouter as DefaultRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append('.')


# python-multipart, construct 2.5.3, fastapi

app = FastAPI()

app.include_router(DefaultRouter.router)
app.include_router(ParsingRouter.router)
app.include_router(ApkRouter.router)

origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
