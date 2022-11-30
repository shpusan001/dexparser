from struct import *

from src.exception.UserException import UserUtilException

# 해당 바이트가 LEB128포맷의 마지막인지 반환
def isEndOfLEB128(b:bytes)->bool:
    if len(b) != 1:
        raise UserUtilException("Scan with only one byte.")
    
    byte = unpack(">b", b)[0]

    mask = 128

    maskedValue = byte & mask

    # 10000000
    if maskedValue == 128: 
        return False
    else:
        return True

# LEB128의 바이트 크기 반환
def getSizeOfLEB128(fp, off:int)->int:
    size = 0
    fp.seek(off)

    while True:
        size+=1
        if isEndOfLEB128(fp.read(1)):
            break
    
    fp.seek(off)

    return size
    