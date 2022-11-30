import pprint
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

    def getStringIds(self) -> list:
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
            stringIdsOffs.append({"string_data_off":unpack("<I", fp.read(STRING_ID_ITEM_SIZE))[0]})

        fp.close()
        return stringIdsOffs

    def getStringFull(self) -> list:
        res = list()
        stringIds = self.getStringIds()
        fp = self.getfp('rb')

        for idx in stringIds:
            off = idx["string_data_off"]

            fp.seek(off)
            # 스트링의 크기를 나타내는 데이터의 크기 
            LEB128Size = getSizeOfLEB128(fp, off)

            # 스트링의 크기
            stringSize = unpack(str(LEB128Size) + "s", fp.read(LEB128Size))[0]
            stringSize = leb128.u.decode(stringSize)


            res.append({"string_data_full" : unpack(str(stringSize)+"s", fp.read(stringSize))[0].decode("utf-8")})
        
        fp.close()

        return res

    def getTypeIds(self)->list:
        TYPE_ID_ITEM_SIZE = 4

        res = list()

        headers = self.getHeader()

        typeIdsSize = unpack("<I", headers["type_ids_size"])[0]
        typeIdsOff = unpack("<I", headers["type_ids_off"])[0]

        fp = fp = self.getfp('rb')

        if typeIdsOff == 0:
            return res

        fp.seek(typeIdsOff)

        for _ in range(typeIdsSize):
            typeIdItem = fp.read(TYPE_ID_ITEM_SIZE)
            typeIdItem = unpack("<I", typeIdItem)[0]
            res.append({"descriptor_idx": typeIdItem})
        
        return res

    def getTypeFull(self)->list:
        TYPE_ID_ITEM_SIZE = 4

        res = list()

        headers = self.getHeader()
        stringFull = self.getStringFull()

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
            res.append({"descriptor_full":stringFull[typeIdItem]})
        
        fp.close()

        return res

    def getProtoIds(self)->list:
        headers = self.getHeader()

        res = list()

        protoIdsSize = unpack("<I", headers["proto_ids_size"])[0]
        protoIdsOff = unpack("<I", headers["proto_ids_off"])[0]

        if protoIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(protoIdsOff)

        for _ in range(protoIdsSize):
            fieldIdItem = dict()
            fieldIdItem["shorty_idx"] = unpack("<I", fp.read(4))[0]
            fieldIdItem["return_type_idx"] = unpack("<I", fp.read(4))[0]
            fieldIdItem["parameters_off"] = unpack("<I", fp.read(4))[0]
            res.append(fieldIdItem)

        fp. close()

        return res

    def getTypeListIds(self, fp, off:int)->list:
        res = list()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]
        
        for _ in range(size):
            res.append(unpack("<H", fp.read(2))[0])
        
        fp.seek(off)
        return res

    def getTypeListFull(self, fp, off:int)->list:
        res = list()

        typeIds = self.getTypeIds()
        stringFull = self.getStringFull()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]
        
        for _ in range(size):
            typeIdx = unpack("<H", fp.read(2))[0]
            print(typeIdx)
            # stringIdx = typeIds[typeIdx]["descriptor_idx"]
            # string = stringFull[stringIdx]["string_data_full"]
            # res.append(string)
        
        fp.seek(off)
        return res
        
    
    def getProtoFull(self)->list:
        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        protoIds = self.getProtoIds()

        fp = self.getfp('rb')
        
        for proto in protoIds:
            print(proto["shorty_idx"])
            proto["shorty_idx"] = stringFull[proto["shorty_idx"]]["string_data_full"]
            proto["return_type_idx"] = stringFull[typeIds[proto["return_type_idx"]]["descriptor_idx"]]["string_data_full"]
            fp.seek(proto["parameters_off"])
            proto["parameters_off"] = self.getTypeListFull(fp, proto["parameters_off"])
            pass
        res = protoIds
        pprint.pprint(res)

        fp.close()
        return res

    def getClasses(self):

        res = list()

        headers = self.getHeader()

        classDefsSize = headers["class_defs_size"]
        classDefsOffset = headers["class_defs_off"]

        fp = self.getfp('rb')
        fp.seek(0)
        fp.close()
