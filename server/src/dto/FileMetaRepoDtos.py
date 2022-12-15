from pydantic import BaseModel


class FileMeta(BaseModel):
    fileName: str
    fileId: str
    sha1: str
