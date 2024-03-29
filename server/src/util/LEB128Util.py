import leb128
from struct import *


class LEB128Util:

    # 해당 바이트가 LEB128포맷의 마지막인지 반환
    def __isEndOfLEB128(self, b: bytes) -> bool:

        byte = unpack(">b", b)[0]

        mask = 128

        maskedValue = byte & mask

        # 10000000
        if maskedValue == 128:
            return False
        else:
            return True

    # LEB128의 바이트 크기 반환
    def getSizeOfLEB128(self, fp, off: int) -> int:
        size = 0
        fp.seek(off)

        while True:
            size += 1
            if self.__isEndOfLEB128(fp.read(1)):
                break

        fp.seek(off)

        return size

    def readLEB128ToInt(self, fp, off: int) -> int:

        fp.seek(off)
        # 크기를 나타내는 데이터의 크기
        LEB128Size = self.getSizeOfLEB128(fp, off)

        res = unpack(str(LEB128Size) + "s", fp.read(LEB128Size))[0]
        res = leb128.u.decode(res)
        return res

    def readSLEB128ToInt(self, fp, off: int) -> int:

        fp.seek(off)
        # 크기를 나타내는 데이터의 크기
        LEB128Size = self.getSizeOfLEB128(fp, off)

        res = unpack(str(LEB128Size) + "s", fp.read(LEB128Size))[0]
        res = leb128.i.decode(res)
        return res
