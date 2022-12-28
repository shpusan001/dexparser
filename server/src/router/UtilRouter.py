from fastapi import APIRouter
from src.dto.FileManagerServiceDtoes import *
import time


class UtilRouter():

    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route("/sync", self.sync, methods=["GET"])

    def sync(self):
        nstime = time.time_ns()
        return {"time": nstime, "sync": "sync"}
