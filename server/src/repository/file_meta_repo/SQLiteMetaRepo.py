from typing import List
from typing import Optional
from src.dto.FileMetaRepoDtos import FileMeta
from src.repository.file_meta_repo.FileMetaRepo import FileMetaRepo
import os
import sqlite3


class SQLiteMetaRepo(FileMetaRepo):
    def __init__(self) -> None:
        self.WORK_DIR = "./work"
        self.DB_DIR = self.WORK_DIR + "/db"

        try:
            if not os.path.isdir(self.WORK_DIR):
                os.mkdir(self.WORK_DIR)

            if not os.path.isdir(self.DB_DIR):
                os.mkdir(self.DB_DIR)
        except:
            pass

        self.con = sqlite3.connect(
            self.DB_DIR + "/dex_parser.sqlite")
        cur = self.con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS file_meta_repo(file_id text, file_name text, sha1 text)")

    def createFileMeta(self, fileId: str, meta: FileMeta) -> bool:
        con = self.con
        con.execute("INSERT INTO file_meta_repo VALUES(?, ?, ?)",
                    (fileId, meta.fileName, meta.sha1))
        con.commit()

    def deleteFileMeta(self, fileId: str) -> bool:
        con = self.con
        con.execute(
            "DELETE FROM file_meta_repo WHERE file_id = ?", (fileId,))
        con.commit()

    def readFileMetaes(self) -> List[FileMeta]:
        cur = self.con.cursor()
        cur.execute(
            "SELECT file_id, file_name, sha1 FROM file_meta_repo")
        dataList = cur.fetchall()

        res = list()

        for data in dataList:
            dto = {
                "fileId": data[0],
                "fileName": data[1],
                "sha1": data[2]
            }
            res.append(FileMeta(**dto))

        return res

    def readFileMeta(self, fileId: str) -> Optional[FileMeta]:
        cur = self.con.cursor()
        cur.execute(
            "SELECT file_id, file_name, sha1 FROM file_meta_repo WHERE file_id = ?", (fileId,))
        data = cur.fetchone()

        if data == None:
            return None

        dto = {
            "fileId": data[0],
            "fileName": data[1],
            "sha1": data[2]
        }

        return FileMeta(**dto)
