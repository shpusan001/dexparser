class DexPaser:
    def __init__(self) -> None:
        self.dirpath=None
        self.filepath=None
        pass

    def setFile(self, dirpath:str, filename:str) -> None:
        self.dirpath = dirpath
        self.filename = filename
    
    def parseHeader(self) -> dict:
        
        res = dict()

        fp = open(self.dirpath + self.filename, 'rb')
        fp.seek(0)

        res["Magic"] = fp.read(8)
        res["Checksum"] = fp.read(4)
        res["Signature"] = fp.read(20)
        res["file_size"] = fp.read(4)
        res["file_header_size"] = fp.read(4)
        res["endian_tag"] = fp.read(4)
        res["link_size"] = fp.read(4)
        res["link_offset"] = fp.read(4)
        res["map_off"] = fp.read(4)
        

        return res
    
    
        
