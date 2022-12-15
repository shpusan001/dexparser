from typing import Any, Optional
from pydantic import BaseModel

from src.dto.FileMetaRepoDtos import FileMeta


class UploadApkRes(BaseModel):
    data: Optional[FileMeta]
    isError: str
    error: Optional[Any]


class DeleteApkRes(BaseModel):
    data: Optional[FileMeta]
    isError: str
    error: Optional[Any]
