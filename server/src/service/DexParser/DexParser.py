from struct import *
import leb128
import sys
sys.path.append('.')

from src.util.LEB128Util import getSizeOfLEB128



class DexPaser:
    def __init__(self) -> None:
        self.dirpath = None
        self.filepath = None
        pass

    def setFile(self, dirpath: str, filename: str) -> None:
        self.dirpath = dirpath
        self.filename = filename

    def getfp(self, mode: str):
        return open(self.dirpath + self.filename, mode)

    # 덱스 헤더를 파싱하고 dict로 반환한다
    # 헤더 아이템 정의 : https://source.android.com/docs/core/dalvik/dex-format?hl=ko#header-item
    def getHeader(self) -> dict:

        # format: (name, readsize)
        headerNames = [
            ("magic", 8), ("checksum", 4), ("signature", 20), ("file_size", 4),
            ("header_size", 4), ("endian_tag", 4), ("link_size", 4), ("link_off", 4),
            ("map_off", 4), ("string_ids_size", 4), ("string_ids_off", 4), ("type_ids_size", 4),
            ("type_ids_off", 4), ("proto_ids_size", 4), ("proto_ids_off", 4), ("field_ids_size", 4),
            ("field_ids_off", 4), ("method_ids_size", 4), ("method_ids_off", 4), ("class_defs_size", 4),
            ("class_defs_off", 4), ("data_size", 4), ("data_off", 4)
        ]
        res = dict()

        fp = self.getfp('rb')
        fp.seek(0)

        for name in headerNames:
            res[name[0]] = fp.read(name[1])

        fp.close()
        return res

    def getStringIndexes(self) -> list:
        STRING_ID_ITEM_SIZE = 4

        fp = self.getfp('rb')
        headers = self.getHeader()
        stringIdsSize = unpack("<I", headers["string_ids_size"])[0]
        stringIdsOff = unpack("<I", headers["string_ids_off"])[0]
        stringIdsOffs = list()

        if stringIdsOff == 0:
            return stringIdsOff

        # goto string_ids_off
        fp.seek(stringIdsOff)

        for _ in range(stringIdsSize):
            stringIdsOffs.append(unpack("<I", fp.read(STRING_ID_ITEM_SIZE))[0])

        fp.close()
        return stringIdsOffs

    def getStringDataes(self) -> list:
        res = list()
        stringIndexes = self.getStringIndexes()
        fp = self.getfp('rb')

        for off in stringIndexes:
            fp.seek(off)
            # 스트링의 크기를 나타내는 데이터의 크기 
            LEB128Size = getSizeOfLEB128(fp, off)

            # 스트링의 크기
            stringSize = unpack(str(LEB128Size) + "s", fp.read(LEB128Size))[0]
            stringSize = leb128.u.decode(stringSize)


            res.append(unpack(str(stringSize)+"s", fp.read(stringSize))[0].decode("utf-8"))
        
        fp.close()

        return res

    def getTypeIds(self)->list:
        TYPE_ID_ITEM_SIZE = 4

        res = list()

        headers = self.getHeader()
        stringDataes = self.getStringDataes()

        typeIdsSize = unpack("<I", headers["type_ids_size"])[0]
        typeIdsOff = unpack("<I", headers["type_ids_off"])[0]

        fp = fp = self.getfp('rb')

        if typeIdsOff == 0:
            return res

        fp.seek(typeIdsOff)

        for _ in range(typeIdsSize):
            typeIdItem = fp.read(TYPE_ID_ITEM_SIZE)
            typeIdItem = unpack("<I", typeIdItem)[0]
            res.append(typeIdItem)
        
        return res

    def getTypeStringDataes(self)->list:
        TYPE_ID_ITEM_SIZE = 4

        res = list()

        headers = self.getHeader()
        stringDataes = self.getStringDataes()

        typeIdsSize = unpack("<I", headers["type_ids_size"])[0]
        typeIdsOff = unpack("<I", headers["type_ids_off"])[0]

        fp = fp = self.getfp('rb')

        if typeIdsOff == 0:
            return res

        fp.seek(typeIdsOff)
        
        res = list()

        for _ in range(typeIdsSize):
            typeIdItem = fp.read(TYPE_ID_ITEM_SIZE)
            typeIdItem = unpack("<I", typeIdItem)[0]
            res.append(stringDataes[typeIdItem])
        
        return res

    def getProtoes(self):
        headers = self.getHeader()
        stringDataes = self.getStringDataes()
        typeIds = self.getTypeIds()

        typeIdsSize = unpack("<I", headers["type_ids_size"])[0]
        typeIdsOff = unpack("<I", headers["type_ids_off"])[0]

        

    def getClasses(self):

        res = list()

        headers = self.getHeader()

        classDefsSize = headers["class_defs_size"]
        classDefsOffset = headers["class_defs_off"]

        fp = self.getfp('rb')
        fp.seek(0)
