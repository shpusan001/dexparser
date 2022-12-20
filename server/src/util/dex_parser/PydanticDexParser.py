from src.util.DexDecompiler import *
from src.util.DexCodes import *
from src.util.LEB128Util import *
import pprint
from struct import *
import leb128
import sys
from src.dto.DexparserDtoes import *
from typing import List
from src.util.dex_parser.DexParser import DexParser
from src.container.RepoContainer import RepoContainer

sys.path.append('.')


NO_INDEX = 4294967295


class PydanticDexParser(DexParser):
    def __init__(self) -> None:
        self.progressRepo = RepoContainer().getProgressRepo()
        self.leb128Util: LEB128Util = LEB128Util()

        self.reqKey: str = "default"

        self.path: str = None
        self.dirpath: str = None

        self.pathType: str = "ONE"  # ONE or TWO

        self.header: Header = None
        self.stringFull: List(StringDataFull) = None
        self.typeIds: List[TypeIdx] = None
        self.typeFull: List[TypeIdxFull] = None
        self.protoIds: List[ProtoIdx] = None
        self.protoFull: List[ProtoFull] = None

        self.dexDecompiler = DexDecompiler()
        self.typeListCache = dict()

    def setReqKey(self, reqKey: str) -> None:
        self.reqKey = reqKey

    def setFileFullPath(self, path) -> None:
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

    def getParsedData(self) -> dict:
        return self.getClassFull()

    # 덱스 헤더를 파싱하고 dict로 반환한다
    # 헤더 아이템 정의 : https://source.android.com/docs/core/dalvik/dex-format?hl=ko#header-item
    def getHeader(self) -> Header:

        if self.header != None:
            return self.header

        # format: (name, readsize)
        headerNames = [
            ("magic", 8, "bytes"), ("checksum", 4, "bytes"), ("signature",
                                                              20, "bytes"), ("file_size", 4, "int"),
            ("header_size", 4, "int"), ("endian_tag",
                                        4, "bytes"), ("link_size", 4, "int"), ("link_off", 4, "int"),
            ("map_off", 4, "int"), ("string_ids_size",
                                    4, "int"), ("string_ids_off", 4, "int"), ("type_ids_size", 4, "int"),
            ("type_ids_off", 4, "int"), ("proto_ids_size",
                                         4, "int"), ("proto_ids_off", 4, "int"), ("field_ids_size", 4, "int"),
            ("field_ids_off", 4, "int"), ("method_ids_size",
                                          4, "int"), ("method_ids_off", 4, "int"), ("class_defs_size", 4, "int"),
            ("class_defs_off", 4, "int"), ("data_size",
                                           4, "int"), ("data_off", 4, "int")
        ]
        res = dict()

        fp = self.getfp('rb')
        fp.seek(0)

        for name in headerNames:
            if name[2] == "bytes":
                res[name[0]] = fp.read(name[1])
            elif name[2] == "int":
                res[name[0]] = unpack("<I", fp.read(name[1]))[0]
        fp.close()

        res = Header(**res)

        return res

    def getStringIds(self) -> List[StringDataOff]:

        fp = self.getfp('rb')
        headers = self.getHeader()
        stringIdsSize = headers.string_ids_size
        stringIdsOff = headers.string_ids_off
        res = list()

        if stringIdsOff == 0:
            return stringIdsOff

        # goto string_ids_off
        fp.seek(stringIdsOff)

        for _ in range(stringIdsSize):
            data = {"string_data_off": unpack(
                "<I", fp.read(4))[0]}
            stringDataOff = StringDataOff(**data)
            res.append(stringDataOff)

        fp.close()
        return res

    def getStringFull(self) -> List[StringDataFull]:

        if self.stringFull != None:
            return self.stringFull

        res = list()
        stringIds = self.getStringIds()
        fp = self.getfp('rb')

        for stringIdx in stringIds:
            off = stringIdx.string_data_off

            fp.seek(off)
            # 스트링의 크기를 나타내는 데이터의 크기
            LEB128Size = self.leb128Util.getSizeOfLEB128(fp, off)

            # 스트링의 크기
            stringSize = unpack(str(LEB128Size) + "s", fp.read(LEB128Size))[0]
            stringSize = leb128.u.decode(stringSize)

            data = {"string_data_full": unpack(
                str(stringSize)+"s", fp.read(stringSize))[0].decode('latin_1')}
            string_data_full = StringDataFull(**data)
            res.append(string_data_full)

        fp.close()

        self.stringFull = res

        return res

    def getTypeIds(self) -> List[TypeIdx]:

        if self.typeIds != None:
            return self.typeIds

        TYPE_ID_ITEM_SIZE = 4

        res = list()

        headers = self.getHeader()

        typeIdsSize = headers.type_ids_size
        typeIdsOff = headers.type_ids_off

        fp = fp = self.getfp('rb')

        if typeIdsOff == 0:
            return res

        fp.seek(typeIdsOff)

        for _ in range(typeIdsSize):
            readData = unpack("<I", fp.read(TYPE_ID_ITEM_SIZE))[0]
            typeIdxData = {"descriptor_idx": readData}

            typeIdx = TypeIdx(**typeIdxData)
            res.append(typeIdx)

        fp.close()

        return res

    def getTypeFull(self) -> List[TypeIdxFull]:

        if self.typeFull != None:
            return self.typeFull

        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()

        fp = fp = self.getfp('rb')

        res = list()

        for typeIdx in typeIds:
            typeStringData = stringFull[typeIdx.descriptor_idx]
            typeIdxFullData = {
                "descriptor_full": typeStringData.string_data_full}
            typeIdxFull = TypeIdxFull(**typeIdxFullData)
            res.append(typeIdxFull)

        fp.close()

        self.typeFull = res

        return res

    def getProtoIds(self) -> List[ProtoIdx]:

        if self.protoIds != None:
            return self.protoIds

        headers = self.getHeader()

        res = list()

        protoIdsSize = headers.proto_ids_size
        protoIdsOff = headers.proto_ids_off

        if protoIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(protoIdsOff)

        for _ in range(protoIdsSize):
            protoIdxData = dict()
            protoIdxData["shorty_idx"] = unpack("<I", fp.read(4))[0]
            protoIdxData["return_type_idx"] = unpack("<I", fp.read(4))[0]
            protoIdxData["parameters_off"] = unpack("<I", fp.read(4))[0]

            protoIdx = ProtoIdx(**protoIdxData)

            res.append(protoIdx)

        fp. close()

        return res

    def getTypeListIds(self, fp, off: int) -> List[TypeListIdx]:
        res = list()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]

        for _ in range(size):
            readData = unpack("<H", fp.read(2))[0]
            typeListIdxData = {"type_list_idx": readData}
            typeListIdx = TypeListIdx(**typeListIdxData)
            res.append(typeListIdx)

        fp.seek(off)
        return res

    def convertTypeIdxToString(self, typeIdx: int, stringFull: List[StringDataFull], typeIds: List[TypeIdx]) -> str:
        descritor_idx = typeIds[typeIdx].descriptor_idx
        res = stringFull[descritor_idx].string_data_full
        if res[0] not in ("L", "["):
            return TYPE_DESCRIPTOR[res[0]]
        else:
            return res[1:]

    def getTypeListFulls(self, fp, off: int) -> List[str]:
        res = list()

        if off in self.typeListCache:
            return self.typeListCache[off]

        typeIds = self.getTypeIds()
        stringFull = self.getStringFull()

        fp.seek(off)

        size = unpack("<I", fp.read(4))[0]

        for _ in range(size):

            readData = unpack("<H", fp.read(2))[0]
            typeListIdxData = {"type_list_idx": readData}
            typeListIdx = TypeListIdx(**typeListIdxData)

            string = self.convertTypeIdxToString(
                typeListIdx.type_list_idx, stringFull, typeIds)
            # typeListFullData = {"type_list_full": string}
            # typeListFull = TypeListFull(**typeListFullData)
            res.append(string)
        fp.seek(off)

        self.typeListCache[off] = res
        return res

    def getProtoFull(self) -> List[ProtoFull]:

        if self.protoIds != None:
            return self.protoIds

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        protoIds = self.getProtoIds()

        fp = self.getfp('rb')

        res = list()

        for protoIdx in protoIds:
            protoFullData = dict()
            protoFullData["shorty"] = self.converStringIdxToString(
                protoIdx.shorty_idx, stringFull)

            protoFullData["return_type"] = self.convertTypeIdxToString(
                protoIdx.return_type_idx, stringFull, typeIds)

            if protoIdx.parameters_off == 0:
                protoFullData["parameters"] = []
            else:
                protoFullData["parameters"] = self.getTypeListFulls(
                    fp, protoIdx.parameters_off)

            protoFull = ProtoFull(**protoFullData)
            res.append(protoFull)
            self.progressRepo.updateProgress(self.reqKey)

        fp.close()

        self.protoFull = res

        return res

    def getFieldIds(self) -> List[FieldIdx]:
        headers = self.getHeader()

        res = list()

        fieldIdsSize = headers.field_ids_size
        fieldIdsOff = headers.field_ids_off
        if fieldIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(fieldIdsOff)

        for _ in range(fieldIdsSize):
            fieldIdxData = dict()
            fieldIdxData["class_idx"] = unpack("<H", fp.read(2))[0]
            fieldIdxData["type_idx"] = unpack("<H", fp.read(2))[0]
            fieldIdxData["name_idx"] = unpack("<I", fp.read(4))[0]

            fieldIdx = FieldIdx(**fieldIdxData)
            res.append(fieldIdx)

        fp. close()

        return res

    def getFieldFull(self) -> List[FieldFull]:
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        fieldIds = self.getFieldIds()

        for field in fieldIds:
            fieldFullData = dict()
            fieldFullData["clazz"] = self.convertTypeIdxToString(
                field.class_idx, stringFull, typeIds)
            fieldFullData["type_full"] = self.convertTypeIdxToString(
                field.type_idx, stringFull, typeIds)
            fieldFullData["name"] = self.converStringIdxToString(
                field.name_idx, stringFull)

            fieldFull = FieldFull(**fieldFullData)
            res.append(fieldFull)

        return res

    def getMethodIds(self) -> List[MethodIdx]:
        headers = self.getHeader()

        res = list()

        methodIdsSize = headers.method_ids_size
        methodIdsOff = headers.method_ids_off

        if methodIdsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(methodIdsOff)

        for _ in range(methodIdsSize):
            methodIdxData = dict()
            methodIdxData["class_idx"] = unpack("<H", fp.read(2))[0]
            methodIdxData["proto_idx"] = unpack("<H", fp.read(2))[0]
            methodIdxData["name_idx"] = unpack("<I", fp.read(4))[0]

            methodIdx = MethodIdx(**methodIdxData)
            res.append(methodIdx)

        fp. close()

        return res

    def getMethodFull(self) -> List[MethodFull]:
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        protoFull = self.getProtoFull()
        methodIds = self.getMethodIds()

        for method in methodIds:
            methodFullData = dict()
            methodFullData["clazz"] = self.convertTypeIdxToString(
                method.class_idx, stringFull, typeIds)
            methodFullData["proto"] = protoFull[method.proto_idx]
            methodFullData["name"] = self.converStringIdxToString(
                method.name_idx, stringFull)

            methodFull = MethodFull(**methodFullData)
            res.append(methodFull)

        return res

    def getClassIds(self) -> List[ClassIdx]:

        headers = self.getHeader()

        res = list()

        classDefsSize = headers.class_defs_size
        classDefsOff = headers.class_defs_off

        if classDefsOff == 0:
            return res

        fp = self.getfp('rb')

        fp.seek(classDefsOff)

        for _ in range(classDefsSize):
            classIdsData = dict()
            classIdsData["class_idx"] = unpack("<I", fp.read(4))[0]
            classIdsData["access_flags"] = unpack("<I", fp.read(4))[0]
            classIdsData["superclass_idx"] = unpack("<I", fp.read(4))[0]
            classIdsData["interfaces_off"] = unpack("<I", fp.read(4))[0]
            classIdsData["source_file_idx"] = unpack("<I", fp.read(4))[0]
            classIdsData["annotation_off"] = unpack("<I", fp.read(4))[0]
            classIdsData["class_data_off"] = unpack("<I", fp.read(4))[0]
            classIdsData["static_values_off"] = unpack("<I", fp.read(4))[0]

            classIds = ClassIdx(**classIdsData)

            res.append(classIds)

        fp. close()
        return res

    # def getAnnotDirItem(self, fp, off:int)->dict:

    #     fp.seek(off)

    #     annotDirItem = dict()
    #     annotDirItem["class_annotations_off"] = unpack("<I", fp.read(4))[0]
    #     annotDirItem["access_flags"] = unpack("<I", fp.read(4))[0]

    def readStaticFields(self, fp, off: int, size: int, dataPack: ClassDataPack) -> List[StaticField]:

        fp.seek(off)

        fieldFull = dataPack.fieldFull

        res = list()

        fields = list()

        for _ in range(size):
            encodedField = dict()

            encodedField["field_idx_diff"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["access_flags"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()

            fields.append(encodedField)

        tmp = 0
        for i in range(len(fields)):
            if i == 0:
                tmp = fields[i]["field_idx_diff"]
                fields[i]["field"] = fieldFull[tmp]
            else:
                tmp += fields[i]["field_idx_diff"]
                fields[i]["field"] = fieldFull[tmp]

            fields[i]["access_flags"] = self.convertAccessFlagToString(
                fields[i]["access_flags"], ACCESS_FLAG)

            del fields[i]["field_idx_diff"]

            staticFieldData = fields[i]
            staticField = StaticField(**staticFieldData)
            res.append(staticField)

        return res

    def readInstanceFields(self, fp, off: int, size: int, dataPack: ClassDataPack) -> List[InstanceField]:
        fp.seek(off)

        fieldFull = dataPack.fieldFull

        res = list()

        fields = list()

        for _ in range(size):
            encodedField = dict()

            encodedField["field_idx_diff"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["access_flags"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()

            fields.append(encodedField)

        tmp = 0
        for i in range(len(fields)):
            if i == 0:
                tmp = fields[i]["field_idx_diff"]
                fields[i]["field"] = fieldFull[tmp]
            else:
                tmp += fields[i]["field_idx_diff"]
                fields[i]["field"] = fieldFull[tmp]

            fields[i]["access_flags"] = self.convertAccessFlagToString(
                fields[i]["access_flags"], ACCESS_FLAG)

            del fields[i]["field_idx_diff"]

            instanceFieldData = fields[i]
            instanceField = InstanceField(**instanceFieldData)
            res.append(instanceField)

        return res

    def getTryItem(self, fp, off: int) -> TryItem:

        fp.seek(off)

        tryItemData = dict()

        tryItemData["start_addr"] = unpack("<I", fp.read(4))[0]
        tryItemData["insn_count"] = unpack("<H", fp.read(2))[0]
        tryItemData["handler_off"] = unpack("<H", fp.read(2))[0]

        tryItem = TryItem(**tryItemData)

        return tryItem

    def getEncodedTypeAddrPair(self, fp, off: int) -> EncodedTypeAddrPair:
        fp.seek(off)

        encodedTypeAddrPairData = dict()

        encodedTypeAddrPairData["type_idx"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()
        encodedTypeAddrPairData["addr"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()

        encodedTypeAddrPair = EncodedTypeAddrPair(**encodedTypeAddrPairData)

        return encodedTypeAddrPair

    def getEncodedCatchHandler(self, fp, off: int) -> EncodedCatchHandler:

        fp.seek(off)

        encodedCatchHandlerData = dict()

        encodedCatchHandlerData["size"] = self.leb128Util.readSLEB128ToInt(
            fp, off)
        off = fp.tell()

        encodedTypeAddrPairList = list()
        for _ in range(abs(encodedCatchHandlerData["size"])):
            encodedTypeAddrPairList.append(
                self.getEncodedTypeAddrPair(fp, off))
        encodedCatchHandlerData["handlers"] = encodedTypeAddrPairList

        if encodedCatchHandlerData["size"] < 0:
            encodedCatchHandlerData["catch_all_addr"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
        else:
            encodedCatchHandlerData["catch_all_addr"] = -1

        encodedCatchHandler = EncodedCatchHandler(**encodedCatchHandlerData)

        return encodedCatchHandler

    def getEncodedCatchHandlerList(self, fp, off: int) -> EncodedCatchHandlerList:

        fp.seek(off)

        encodedCatchHandlerListData = dict()

        encodedCatchHandlerListData["size"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()

        handlerList = list()
        for _ in range(encodedCatchHandlerListData["size"]):
            handlerList.append(self.getEncodedCatchHandler(fp, off))
        encodedCatchHandlerListData["handler_list"] = handlerList

        encodedCatchHandlerList = EncodedCatchHandlerList(
            **encodedCatchHandlerListData)

        return encodedCatchHandlerList

    def getCodeItem(self, fp, off: int) -> CodeItem:

        fp.seek(off)

        CodeItemData = dict()

        CodeItemData["register_size"] = unpack("<H", fp.read(2))[0]
        CodeItemData["ins_size"] = unpack("<H", fp.read(2))[0]
        CodeItemData["outs_size"] = unpack("<H", fp.read(2))[0]
        CodeItemData["tries_size"] = unpack("<H", fp.read(2))[0]
        CodeItemData["debug_into_off"] = unpack("<I", fp.read(4))[0]
        CodeItemData["insns_size"] = unpack("<I", fp.read(4))[0]

        tmp = str()
        for i in range(CodeItemData["insns_size"]):
            tmp = tmp + fp.read(2).hex()

        CodeItemData["insns"] = tmp

        if CodeItemData["tries_size"] != 0 and CodeItemData["insns_size"] % 2 == 1:
            CodeItemData["padding"] = unpack("<H", fp.read(2))[0]

        tmp = list()
        for _ in range(CodeItemData["tries_size"]):
            tmp.append(self.getTryItem(fp, fp.tell()))
        CodeItemData["tries"] = tmp

        if CodeItemData["tries_size"] != 0:
            CodeItemData["handler"] = self.getEncodedCatchHandlerList(
                fp, fp.tell())

        codeItem = CodeItem(**CodeItemData)

        return codeItem

    def readDirectMethods(self, fp, off: int, size: int, dataPack: ClassDataPack) -> List[DirectMethod]:
        fp.seek(off)

        fields = list()

        res = list()

        methodFull = dataPack.methodFull

        for _ in range(size):
            encodedField = dict()

            encodedField["method_idx_diff"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["access_flags"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["code_off"] = self.leb128Util.readLEB128ToInt(fp, off)
            off = fp.tell()
            fields.append(encodedField)

        tmp = 0
        for i in range(len(fields)):
            if i == 0:
                tmp = fields[i]["method_idx_diff"]
                fields[i]["method"] = methodFull[tmp]
            else:
                tmp += fields[i]["method_idx_diff"]
                fields[i]["method"] = methodFull[tmp]

            fields[i]["access_flags"] = self.convertAccessFlagToString(
                fields[i]["access_flags"], ACCESS_FLAG)

            if fields[i]["code_off"] != 0:
                fields[i]["code"] = self.getCodeItem(fp, fields[i]["code_off"])
            else:
                fields[i]["code"] = None

            del fields[i]["method_idx_diff"]
            del fields[i]["code_off"]

            directMethodData = fields[i]
            directMethod = DirectMethod(**directMethodData)
            res.append(directMethod)

            fp.seek(off)

        return res

    def readVirtualMethods(self, fp, off: int, size: int, dataPack: ClassDataPack) -> List[VirtualMethod]:
        fp.seek(off)

        fields = list()

        res = list()

        methodFull = dataPack.methodFull

        for _ in range(size):
            encodedField = dict()

            encodedField["method_idx_diff"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["access_flags"] = self.leb128Util.readLEB128ToInt(
                fp, off)
            off = fp.tell()
            encodedField["code_off"] = self.leb128Util.readLEB128ToInt(fp, off)
            off = fp.tell()
            fields.append(encodedField)

        tmp = 0
        for i in range(len(fields)):
            if i == 0:
                tmp = fields[i]["method_idx_diff"]
                fields[i]["method"] = methodFull[tmp]
            else:
                tmp += fields[i]["method_idx_diff"]
                fields[i]["method"] = methodFull[tmp]

            fields[i]["access_flags"] = self.convertAccessFlagToString(
                fields[i]["access_flags"], ACCESS_FLAG)

            if fields[i]["code_off"] != 0:
                fields[i]["code"] = self.getCodeItem(fp, fields[i]["code_off"])
            else:
                fields[i]["code"] = None

            del fields[i]["method_idx_diff"]
            del fields[i]["code_off"]

            virtualMethodData = fields[i]
            virtualMethod = VirtualMethod(**virtualMethodData)
            res.append(virtualMethod)

            fp.seek(off)

        return res

    def getClassDataItem(self, fp, off: int, dataPack: ClassDataPack) -> ClassDataItem:

        fp.seek(off)

        classDataItemData = dict()

        classDataItemData["static_fields_size"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()
        classDataItemData["instance_fields_size"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()
        classDataItemData["direct_methods_size"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()
        classDataItemData["virtual_methods_size"] = self.leb128Util.readLEB128ToInt(
            fp, off)
        off = fp.tell()
        classDataItemData["static_fields"] = self.readStaticFields(
            fp, off, classDataItemData["static_fields_size"], dataPack)
        off = fp.tell()
        classDataItemData["instance_fields"] = self.readInstanceFields(
            fp, off, classDataItemData["instance_fields_size"], dataPack)
        off = fp.tell()
        classDataItemData["direct_methods"] = self.readDirectMethods(
            fp, off, classDataItemData["direct_methods_size"], dataPack)
        off = fp.tell()
        classDataItemData["virtual_methods"] = self.readVirtualMethods(
            fp, off, classDataItemData["virtual_methods_size"], dataPack)
        off = fp.tell()

        classDataItem = ClassDataItem(**classDataItemData)

        return classDataItem

    def getClassFull(self) -> dict:
        res = list()

        stringFull = self.getStringFull()
        typeIds = self.getTypeIds()
        fieldFull = self.getFieldFull()
        methodFull = self.getMethodFull()
        classIds = self.getClassIds()

        # 매개 변수에 삽입 할 때  사용
        classDataPackData = dict()
        classDataPackData["stringFull"] = stringFull
        classDataPackData["fieldFull"] = fieldFull
        classDataPackData["methodFull"] = methodFull

        classDataPack = ClassDataPack(**classDataPackData)

        fp = self.getfp("rb")

        for clazz in classIds:
            classFullData = dict()
            classFullData["clazz"] = self.convertTypeIdxToString(
                clazz.class_idx, stringFull, typeIds)
            classFullData["access_flags"] = self.convertAccessFlagToString(
                clazz.access_flags, ACCESS_FLAG)
            classFullData["superclass"] = self.convertTypeIdxToString(
                clazz.superclass_idx, stringFull, typeIds)

            if clazz.interfaces_off == 0:
                classFullData["interfaces"] = []
            else:
                classFullData["interfaces"] = self.getTypeListFulls(
                    fp, clazz.interfaces_off)

            if clazz.source_file_idx != NO_INDEX:
                classFullData["source_file"] = self.converStringIdxToString(
                    clazz.source_file_idx, stringFull)
            else:
                classFullData["source_file"] = "NOT_EXIST"

            if clazz.class_data_off != 0:
                classFullData["class_data"] = self.getClassDataItem(
                    fp, clazz.class_data_off, classDataPack)
            else:
                classFullData["class_data"] = None

            classFull = ClassFull(**classFullData)
            classFullDict: dict = classFull.dict()
            res.append(classFullDict)

            self.progressRepo.updateProgress(self.reqKey)

        fp.close()

        return res

    def converStringIdxToString(self, stringIdx: int, stringFull: List[StringDataFull]) -> str:
        res = stringFull[stringIdx].string_data_full
        return res

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
