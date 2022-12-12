from pydantic import BaseModel
from typing import List


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
    descriptor_full:str

class ProtoIdx(BaseModel):
    shorty_idx:int
    return_type_idx:int
    parameters_off:int

class TypeListIdx(BaseModel):
    type_list_idx: int

class TypeListFull(BaseModel):
    type_list_full: str

class ProtoFull(BaseModel):
    shorty:str
    return_type:str
    parameters: List[TypeListFull]