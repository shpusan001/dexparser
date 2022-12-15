from pydantic import BaseModel
from typing import List, Optional


class Header(BaseModel):
    magic: bytes
    checksum: bytes
    signature: bytes
    file_size: int
    header_size: int
    endian_tag: bytes
    link_size: int
    link_off: int
    map_off: int
    string_ids_size: int
    string_ids_off: int
    type_ids_size: int
    type_ids_off: int
    proto_ids_size: int
    proto_ids_off: int
    field_ids_size: int
    field_ids_off: int
    method_ids_size: int
    method_ids_off: int
    class_defs_size: int
    class_defs_off: int
    data_size: int
    data_off: int


class StringDataOff(BaseModel):
    string_data_off: int


class StringDataFull(BaseModel):
    string_data_full: str


class TypeIdx(BaseModel):
    descriptor_idx: int


class TypeIdxFull(BaseModel):
    descriptor_full: str


class ProtoIdx(BaseModel):
    shorty_idx: int
    return_type_idx: int
    parameters_off: int


class TypeListIdx(BaseModel):
    type_list_idx: int


# class TypeListFull(BaseModel):
#     type_list_full: str


class ProtoFull(BaseModel):
    shorty: str
    return_type: str
    parameters: List[str]


class FieldIdx(BaseModel):
    class_idx: int
    type_idx: int
    name_idx: int


class FieldFull(BaseModel):
    clazz: str
    type_full: str
    name: str


class MethodIdx(BaseModel):
    class_idx: int
    proto_idx: int
    name_idx: int


class MethodFull(BaseModel):
    clazz: str
    proto: ProtoFull
    name: str


class ClassIdx(BaseModel):
    class_idx: int
    access_flags: int
    superclass_idx: int
    interfaces_off: int
    source_file_idx: int
    annotation_off: int
    class_data_off: int
    static_values_off: int


class ClassField(BaseModel):
    field: FieldFull
    access_flags: List[str]


class StaticField(ClassField):
    pass


class InstanceField(ClassField):
    pass


class ClassDataPack(BaseModel):
    stringFull: List[StringDataFull]
    fieldFull: List[FieldFull]
    methodFull: List[MethodFull]


class TryItem(BaseModel):
    start_addr: int
    insn_count: int
    handler_off: int


class EncodedTypeAddrPair(BaseModel):
    type_idx: int
    addr: int


class EncodedCatchHandler(BaseModel):
    size: int
    handlers: List[EncodedTypeAddrPair]
    catch_all_addr: Optional[int] = None


class EncodedCatchHandlerList(BaseModel):
    size: int
    handler_list: List[EncodedCatchHandler]


class CodeItem(BaseModel):
    register_size: int
    ins_size: int
    outs_size: int
    tries_size: int
    debug_into_off: int
    insns_size: int
    insns: str
    padding: Optional[int] = None
    tries: Optional[List[TryItem]] = None
    handlers: Optional[EncodedCatchHandlerList] = None


class ClassMethod(BaseModel):
    method: MethodFull
    access_flags: List[str]
    code: Optional[CodeItem] = None


class DirectMethod(ClassMethod):
    pass


class VirtualMethod(ClassMethod):
    pass


class ClassDataItem(BaseModel):
    static_fields_size: int
    instance_fields_size: int
    direct_methods_size: int
    virtual_methods_size: int
    static_fields: List[StaticField]
    instance_fields: List[InstanceField]
    direct_methods: List[DirectMethod]
    virtual_methods: List[VirtualMethod]


class ClassFull(BaseModel):
    clazz: str
    access_flags: List[str]
    superclass: str
    interfaces: List[str]
    source_file: str
    class_data: Optional[ClassDataItem] = None
