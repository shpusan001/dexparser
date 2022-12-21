from fastapi import APIRouter, Depends
from src.dto.FileManagerServiceDtos import *
from src.util.Singleton import Singleton


class UtilRouter(Singleton):

    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route("/sync", self.sync, methods=["GET"])

    def sync(self):
        return {"sync": "sync"}
