from fastapi import FastAPI
import sys
sys.path.append('.')

import src.router.DefaultRouter as DefaultRouter
import src.router.ParsingRouter as ParsingRouter
import src.router.UploadRouter as UploadRouter

# python-multipart, construct 2.5.3, fastapi

app = FastAPI()

app.include_router(DefaultRouter.router)
app.include_router(ParsingRouter.router)
app.include_router(UploadRouter.router)
