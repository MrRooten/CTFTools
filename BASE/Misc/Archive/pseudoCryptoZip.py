from lib.baseClass import BaseModule
from lib.struct.file.zip import ZIP
from lib.utils import print_error
class Module(BaseModule):
    __info__ = {}
    __options__ = {
        "file_path":{"args":"","necessity":True,"description":"zip path"},
        "save_to":{"args":"","necessity":True,"description":"save to new path"}
    }

    def check(self):
        self.data = open(self.__options__["file_path"]["args"],"rb").read()
        self.zip = ZIP(self.data)
        if int.from_bytes(self.zip.get(ZIP.BIT_FLAG),byteorder='big') == 1:
            return True
        else:
            return False

    def run(self):
        try:
            if self.check():
                self.zip.set(ZIP.BIT_FLAG,b'\x00\x00')
                self.save_file = open(self.__options__["save_to"]["args"],"wb")
                self.save_file.write(self.data)
            else:
                return
        except Exception as e:
            print_error(e)

        finally:
            self.save_file.close()

