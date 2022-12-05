import hashlib

class HashDigester:
    def __init__(self) -> None:
        pass

    def sha1ForLageFile(self, filePath, blockSize=8192):
        sha_1 = hashlib.sha1()
        try:
            f = open(filePath, "rb")
        except IOError as e:
            print("file open error", e)
            return
        while True:
            buf = f.read(blockSize)
            if not buf:
                break
            sha_1.update(buf)
        return sha_1.hexdigest()