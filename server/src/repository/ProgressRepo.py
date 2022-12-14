from src.util.Singleton import Singleton
from src.dto.ProgressDto import ProgressDto
import sqlite3


class ProgressRepo(Singleton):

    def __init__(self) -> None:
        self.con = sqlite3.connect("./progress.ldb")
        cur = self.con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS progress_repo(req_key text, now_value integer, max_value integer)")

    def addProgress(self, reqKey: str, maxValue: int) -> None:
        con = self.con
        con.execute("INSERT INTO progress_repo VALUES(?, ?, ?)",
                    (reqKey, 0, maxValue))
        con.commit()

    def readProgress(self, reqKey: str) -> ProgressDto:
        cur = self.con.cursor()
        cur.execute(
            "SELECT now_value, max_value FROM progress_repo WHERE req_key = ?", (reqKey,))
        data = cur.fetchone()

        if data == None:
            return None

        dto = {
            "nowValue": data[0],
            "maxValue": data[1]
        }
        return ProgressDto(**dto)

    def increaseProgress(self, reqKey: str, value: int = 1) -> None:
        cur = self.con.cursor()
        con = self.con
        cur.execute(
            "SELECT now_value, max_value FROM progress_repo WHERE req_key = ?", (reqKey,))
        data = cur.fetchone()

        if data == None:
            return None

        nowValue = data[0]

        updateValue = nowValue + value
        con.execute(
            "UPDATE progress_repo SET now_value = ? WHERE req_key = ?", (updateValue, reqKey))
        con.commit()

    def removeProgress(self, reqKey: str) -> None:
        con = self.con
        con.execute(
            "DELETE FROM progress_repo WHERE req_key = ?", (reqKey,))
        con.commit()
