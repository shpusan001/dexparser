from src.util.DexDecompiler import *
from src.DexCodes import *
from src.util.LEB128Util import *
import pprint
from struct import *
import leb128
import sys

sys.path.append('.')


NO_INDEX = 4294967295


class DexPaser:
    def __init__(self) -> None:
        self.path = None
        self.dirpath = None
        self.filepath = None

        self.pathType = "ONE"  # ONE or TWO

        self.header = None
        self.stringFull = None
        self.typeIds = None
        self.typeFull = None
        self.protoIds = None
        self.protoFull = None

        self.dexDecompiler = DexDecompiler()
        self.typeListCache = dict()

    def setFileFullPath(self, path):
        self.pathType = "ONE"
        self.path = path

    def setFile(self, dirpath: str, filename: str) -> None:
        self.pathType = "TWO"
        self.dirpath = dirpath
        self.filename = filename

    def getfp(self, mode: str):
        if self.pathType == "ONE":
            return open(self.path, mode)
        elif self.pathType == "TWO":
            return open(self.dirpath + self.filename, mode)
        else:
            raise Exception("pathType is only ONE or TWO")

    # 덱스 헤더를 파싱하고 dict로 반환한다
    # 헤더 아이템 정의 : https://source.android.com/docs/core/dalvik/dex-format?hl=ko#header-item
    def getHeader(self) -> dict:

        if self.header != None:
            return self.header

        # format: (name, readsize)
        headerNames = [
            ("magic", 8), ("checksum", 4), ("signature", 20), ("file_size", 4),
            ("header_size", 4), ("endian_tag",
                                 4), ("link_size", 4), ("link_off", 4),
            ("map_off", 4), ("string_ids_size",
                             4), ("string_ids_off", 4), ("type_ids_size", 4),
            ("type_ids_off", 4), ("proto_ids_size",
                                  4), ("proto_ids_off", 4), ("field_ids_size", 4),
            ("field_ids_off", 4), ("method_ids_size",
                                   4), ("method_ids_off", 4), ("class_defs_size", 4),
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
            stringIdsOffs.append({"string_data_off": unpack(
                "<I", fp.read(STRING_ID_ITEM_SIZE))[0]})

        fp.close()
        return stringIdsOffs

    def getStringFull(self) -> list:

        if self.stringFull != None:
            return self.stringFull

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

            res.append({"string_data_full": unpack(
                str(stringSize)+"s", fp.read(stringSize))[0].decode('latin_1')})

        fp.close()

        self.stringFull = res

        return res

    def getTypeIds(self) -> list:

        if self.typeIds != None:
            return self.typeIds

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

        fp.close()

        return res

    def getTypeFull(self) -> list:

        if self.typeFull != None:
            return self.typeFull

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
            res.append({"descriptor_full": stringFull[typeIdItem]})

        fp.close()

        self.typeFull = res

        return res

    def getProtoIds(self) -> list:

        if self.protoIds != None:
            return self.protoIds

        headers = self.getHeader()

        res = list()

        protoIdsSize = unpack("<I", headers["proto_ids_size"])[0]
        protoIdsOff = unpack("<I", headers["proto_ids_off"])[0]

        if protoIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(protoIdsOff)

        for _ in range(protoIdsSize):
            protoIdItem = dict()
            protoIdItem["shorty_idx"] = unpack("<I", fp.read(4))[0]
            protoIdItem["return_type_idx"] = unpack("<I", fp.read(4))[0]
            protoIdItem["parameters_off"] = unpack("<I", fp.read(4))[0]
            res.append(protoIdItem)

        fp. close()

        return res

    def getTypeListIds(self, fp, off: int) -> list:
        res = list()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]

        for _ in range(size):
            res.append(unpack("<H", fp.read(2))[0])

        fp.seek(off)
        return res

    def getTypeListFull(self, fp, off: int) -> list:
        res = list()

        if off in self.typeListCache:
            return self.typeListCache[off]

        typeIds = self.getTypeIds()
        stringFull = self.getStringFull()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]
        for _ in range(size):
            typeIdx = unpack("<H", fp.read(2))[0]
            string = self.convertTypeIdxToString(typeIdx, stringFull, typeIds)
            res.append(string)
        fp.seek(off)

        self.typeListCache[off] = res
        return res

    def getProtoFull(self) -> list:

        if self.protoIds != None:
            return self.protoIds

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        protoIds = self.getProtoIds()

        fp = self.getfp('rb')

        for proto in protoIds:

            proto["shorty"] = self.converStringIdxToString(
                proto["shorty_idx"], stringFull)

            proto["return_type"] = self.convertTypeIdxToString(
                proto["return_type_idx"], stringFull, typeIds)

            if proto["parameters_off"] == 0:
                proto["parameters"] = []
            else:
                proto["parameters"] = self.getTypeListFull(
                    fp, proto["parameters_off"])

            del proto["shorty_idx"]
            del proto["return_type_idx"]
            del proto["parameters_off"]

        res = protoIds

        fp.close()

        self.protoFull = res

        return res

    def getFieldIds(self) -> list:
        headers = self.getHeader()

        res = list()

        fieldIdsSize = unpack("<I", headers["field_ids_size"])[0]
        fieldIdsOff = unpack("<I", headers["field_ids_off"])[0]

        if fieldIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(fieldIdsOff)

        for _ in range(fieldIdsSize):
            fieldIdItem = dict()
            fieldIdItem["class_idx"] = unpack("<H", fp.read(2))[0]
            fieldIdItem["type_idx"] = unpack("<H", fp.read(2))[0]
            fieldIdItem["name_idx"] = unpack("<I", fp.read(4))[0]
            res.append(fieldIdItem)

        fp. close()

        return res

    def getFieldFull(self) -> list:
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        fieldIds = self.getFieldIds()

        for field in fieldIds:
            fieldFull = dict()
            fieldFull["class"] = self.convertTypeIdxToString(
                field["class_idx"], stringFull, typeIds)
            fieldFull["type"] = self.convertTypeIdxToString(
                field["type_idx"], stringFull, typeIds)
            fieldFull["name"] = self.converStringIdxToString(
                field["name_idx"], stringFull)
            res.append(fieldFull)

        return res

    def getMethodIds(self) -> list:
        headers = self.getHeader()

        res = list()

        methodIdsSize = unpack("<I", headers["method_ids_size"])[0]
        methodIdsOff = unpack("<I", headers["method_ids_off"])[0]

        if methodIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(methodIdsOff)

        for _ in range(methodIdsSize):
            methodIdItem = dict()
            methodIdItem["class_idx"] = unpack("<H", fp.read(2))[0]
            methodIdItem["proto_idx"] = unpack("<H", fp.read(2))[0]
            methodIdItem["name_idx"] = unpack("<I", fp.read(4))[0]
            res.append(methodIdItem)

        fp. close()

        return res

    def getMethodFull(self) -> list:
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        protoFull = self.getProtoFull()
        methodIds = self.getMethodIds()

        for method in methodIds:
            methodFull = dict()
            methodFull["class"] = self.convertTypeIdxToString(
                method["class_idx"], stringFull, typeIds)
            methodFull["proto"] = protoFull[method["proto_idx"]]
            methodFull["name"] = self.converStringIdxToString(
                method["name_idx"], stringFull)
            res.append(methodFull)

        return res

    def getClassIds(self) -> list:

        headers = self.getHeader()

        res = list()

        classDefsSize = unpack("<I", headers["class_defs_size"])[0]
        classDefsOff = unpack("<I", headers["class_defs_off"])[0]

        if classDefsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(classDefsOff)

        for _ in range(classDefsSize):
            classDefItem = dict()
            classDefItem["class_idx"] = unpack("<I", fp.read(4))[0]
            classDefItem["access_flags"] = unpack("<I", fp.read(4))[0]
            classDefItem["superclass_idx"] = unpack("<I", fp.read(4))[0]
            classDefItem["interfaces_off"] = unpack("<I", fp.read(4))[0]
            classDefItem["source_file_idx"] = unpack("<I", fp.read(4))[0]
            classDefItem["annotatios_off"] = unpack("<I", fp.read(4))[0]
            classDefItem["class_data_off"] = unpack("<I", fp.read(4))[0]
            classDefItem["static_values_off"] = unpack("<I", fp.read(4))[0]
            res.append(classDefItem)

        fp. close()
        return res

    # def getAnnotDirItem(self, fp, off:int)->dict:

    #     fp.seek(off)

    #     annotDirItem = dict()
    #     annotDirItem["class_annotations_off"] = unpack("<I", fp.read(4))[0]
    #     annotDirItem["access_flags"] = unpack("<I", fp.read(4))[0]

    def readStaticFields(self, fp, off: int, size: int, dataPack: dict) -> list:

        fp.seek(off)

        res = list()

        fieldFull = dataPack["fieldFull"]

        for _ in range(size):
            encodedField = dict()

            encodedField["field_idx_diff"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["access_flags"] = readLEB128ToInt(fp, off)
            off = fp.tell()

            res.append(encodedField)

        tmp = 0
        for i in range(len(res)):
            if i == 0:
                tmp = res[i]["field_idx_diff"]
                res[i]["field"] = fieldFull[tmp]
            else:
                tmp += res[i]["field_idx_diff"]
                res[i]["field"] = fieldFull[tmp]

            res[i]["access_flags"] = self.convertAccessFlagToString(
                res[i]["access_flags"], ACCESS_FLAG)

            del res[i]["field_idx_diff"]

        return res

    def readInstanceFields(self, fp, off: int, size: int, dataPack: dict) -> list:
        fp.seek(off)

        res = list()

        fieldFull = dataPack["fieldFull"]

        for _ in range(size):
            encodedField = dict()

            encodedField["field_idx_diff"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["access_flags"] = readLEB128ToInt(fp, off)
            off = fp.tell()

            res.append(encodedField)

        tmp = 0
        for i in range(len(res)):
            if i == 0:
                tmp = res[i]["field_idx_diff"]
                res[i]["field"] = fieldFull[tmp]
            else:
                tmp += res[i]["field_idx_diff"]
                res[i]["field"] = fieldFull[tmp]

            res[i]["access_flags"] = self.convertAccessFlagToString(
                res[i]["access_flags"], ACCESS_FLAG)

            del res[i]["field_idx_diff"]

        return res

    def getTryItem(self, fp, off: int) -> dict:

        fp.seek(off)

        res = dict()

        res["start_addr"] = unpack("<I", fp.read(4))[0]
        res["insn_count"] = unpack("<H", fp.read(2))[0]
        res["handler_off"] = unpack("<H", fp.read(2))[0]

        return res

    def getEncodedTypeAddrPair(self, fp, off: int) -> dict:
        fp.seek(off)

        res = dict()

        res["type_idx"] = readLEB128ToInt(fp, off)
        off = fp.tell()
        res["addr"] = readLEB128ToInt(fp, off)
        off = fp.tell()

        return res

    def getEncodedCatchHandler(self, fp, off: int) -> dict:

        fp.seek(off)

        res = dict()

        res["size"] = readSLEB128ToInt(fp, off)
        off = fp.tell()

        tmp = list()
        for _ in range(abs(res["size"])):
            tmp.append(self.getEncodedTypeAddrPair(fp, off))
        res["handlers"] = tmp

        if res["size"] < 0:
            res["catch_all_addr"] = readLEB128ToInt(fp, off)
            off = fp.tell()
        else:
            res["catch_all_addr"] = "NONE"

        return res

    def getEncodedCatchHandlerList(self, fp, off: int) -> dict:

        fp.seek(off)

        res = dict()

        res["size"] = readLEB128ToInt(fp, off)
        off = fp.tell()

        tmp = list()

        for _ in range(res["size"]):
            tmp.append(self.getEncodedCatchHandler(fp, off))
        res["list"] = tmp

        return res

    def getCodeItem(self, fp, off: int) -> dict:

        fp.seek(off)

        res = dict()

        res["register_size"] = unpack("<H", fp.read(2))[0]
        res["ins_size"] = unpack("<H", fp.read(2))[0]
        res["outs_size"] = unpack("<H", fp.read(2))[0]
        res["tries_size"] = unpack("<H", fp.read(2))[0]
        res["debug_into_off"] = unpack("<I", fp.read(4))[0]
        res["insns_size"] = unpack("<I", fp.read(4))[0]

        tmp = str()
        for i in range(res["insns_size"]):
            tmp = tmp + fp.read(2).hex()

        res["insns"] = tmp

        if res["tries_size"] != 0 and res["insns_size"] % 2 == 1:
            res["padding"] = unpack("<H", fp.read(2))[0]

        tmp = list()
        for _ in range(res["tries_size"]):
            tmp.append(self.getTryItem(fp, fp.tell()))
        res["tries"] = tmp

        if res["tries_size"] != 0:
            res["handler"] = self.getEncodedCatchHandlerList(fp, fp.tell())

        return res

    def readDirectMethods(self, fp, off: int, size: int, dataPack: dict) -> list:
        fp.seek(off)

        res = list()

        methodFull = dataPack["methodFull"]

        for _ in range(size):
            encodedField = dict()

            encodedField["method_idx_diff"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["access_flags"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["code_off"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            res.append(encodedField)

        tmp = 0
        for i in range(len(res)):
            if i == 0:
                tmp = res[i]["method_idx_diff"]
                res[i]["method"] = methodFull[tmp]
            else:
                tmp += res[i]["method_idx_diff"]
                res[i]["method"] = methodFull[tmp]

            res[i]["access_flags"] = self.convertAccessFlagToString(
                res[i]["access_flags"], ACCESS_FLAG)
            if res[i]["code_off"] != 0:
                res[i]["code"] = self.getCodeItem(fp, res[i]["code_off"])
            else:
                res[i]["code"] = dict()

            del res[i]["method_idx_diff"]
            del res[i]["access_flags"]
            del res[i]["code_off"]

            fp.seek(off)

        return res

    def readVirtualMethods(self, fp, off: int, size: int, dataPack: dict) -> list:
        fp.seek(off)

        res = list()

        methodFull = dataPack["methodFull"]

        for _ in range(size):
            encodedField = dict()

            encodedField["method_idx_diff"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["access_flags"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            encodedField["code_off"] = readLEB128ToInt(fp, off)
            off = fp.tell()
            res.append(encodedField)

        tmp = 0
        for i in range(len(res)):
            if i == 0:
                tmp = res[i]["method_idx_diff"]
                res[i]["method"] = methodFull[tmp]
            else:
                tmp += res[i]["method_idx_diff"]
                res[i]["method"] = methodFull[tmp]

            res[i]["access_flags"] = self.convertAccessFlagToString(
                res[i]["access_flags"], ACCESS_FLAG)
            if res[i]["code_off"] != 0:
                res[i]["code"] = self.getCodeItem(fp, res[i]["code_off"])
            else:
                res[i]["code"] = dict()

            del res[i]["method_idx_diff"]
            del res[i]["access_flags"]
            del res[i]["code_off"]

            fp.seek(off)

        return res

    def getClassDataItem(self, fp, off: int, dataPack: dict):

        fp.seek(off)

        classDataItem = dict()

        classDataItem["static_fields_size"] = readLEB128ToInt(fp, off)
        off = fp.tell()
        classDataItem["instance_fields_size"] = readLEB128ToInt(fp, off)
        off = fp.tell()
        classDataItem["direct_methods_size"] = readLEB128ToInt(fp, off)
        off = fp.tell()
        classDataItem["virtual_methods_size"] = readLEB128ToInt(fp, off)
        off = fp.tell()
        classDataItem["static_fields"] = self.readStaticFields(
            fp, off, classDataItem["static_fields_size"], dataPack)
        off = fp.tell()
        classDataItem["instance_fields"] = self.readInstanceFields(
            fp, off, classDataItem["instance_fields_size"], dataPack)
        off = fp.tell()
        classDataItem["direct_methods"] = self.readDirectMethods(
            fp, off, classDataItem["direct_methods_size"], dataPack)
        off = fp.tell()
        classDataItem["virtual_methods"] = self.readVirtualMethods(
            fp, off, classDataItem["virtual_methods_size"], dataPack)
        off = fp.tell()

        return classDataItem

    def getClassFull(self):
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        fieldFull = self.getFieldFull()
        methodFull = self.getMethodFull()
        classIds = self.getClassIds()

        # 매개 변수에 삽입 할 때  사용
        classDataPack = dict()
        classDataPack["stringFull"] = stringFull
        classDataPack["fieldFull"] = fieldFull
        classDataPack["methodFull"] = methodFull

        fp = self.getfp("rb")

        for clazz in classIds:
            clazzFull = dict()
            clazzFull["class"] = self.convertTypeIdxToString(
                clazz["class_idx"], stringFull, typeIds)
            clazzFull["access_flags"] = self.convertAccessFlagToString(
                clazz["access_flags"], ACCESS_FLAG)
            clazzFull["superclass"] = self.convertTypeIdxToString(
                clazz["superclass_idx"], stringFull, typeIds)

            if clazz["interfaces_off"] == 0:
                clazzFull["interfaces"] = []
            else:
                clazzFull["interfaces"] = self.getTypeListFull(
                    fp, clazz["interfaces_off"])

            if clazz["source_file_idx"] != NO_INDEX:
                clazzFull["source_file"] = self.converStringIdxToString(
                    clazz["source_file_idx"], stringFull)
            else:
                clazzFull["source_file"] = "NOT_EXIST"

            if clazz["class_data_off"] != 0:
                clazzFull["class_data"] = self.getClassDataItem(
                    fp, clazz["class_data_off"], classDataPack)
            else:
                clazzFull["class_data"] = "NOT_EXIST_CLASSDATA"

            res.append(clazzFull)

        fp.close()

        # with open("result.txt", "w") as external_file:
        #     pprint(res, stream=external_file)
        #     external_file.close()
        return res

    def converStringIdxToString(self, stringIdx: int, stringFull: list) -> str:
        res = stringFull[stringIdx]["string_data_full"]
        return res

    def convertTypeIdxToString(self, typeIdx: int, stringFull: list, typeIds: list) -> str:
        stringIdx = typeIds[typeIdx]["descriptor_idx"]
        res = stringFull[stringIdx]["string_data_full"]
        if res[0] not in ("L", "["):
            return TYPE_DESCRIPTOR[res[0]]
        else:
            return res[1:]

    def convertAccessFlagToString(self, accessFlag: int, accessFlagDict: dict) -> list:

        accessHexes = [0x20000, 0x10000, 0x8000, 0x4000,
                       0x2000, 0x1000, 0x800, 0x400, 0x200, 0x100,
                       0x80, 0x40, 0x20, 0x10, 0x8, 0x4, 0x2, 0x1]

        resHexes = list()
        res = list()

        for ahex in accessHexes:
            if accessFlag >= ahex:
                accessFlag -= ahex
                resHexes.append(ahex)

        for rhex in resHexes:
            res.append(accessFlagDict[rhex])

        return res
