from lib.baseClass import BaseModule
import binascii
import struct
class Module(BaseModule):
    __options__ = {"file":None,"save_to":None}

    def run(self):
        f = open(self.__options__["file"],'rb').read()
        crc32 = binascii.crc32(f[0xc:0xc+17])&0xffffffff
        f[0xc+17:0xc+17+4] = struct.pack('>i',crc32)
        save_file = open(self.__options__["save_to"],'wb')
        save_file.write(f)