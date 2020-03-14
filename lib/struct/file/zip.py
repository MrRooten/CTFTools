import struct
class ZIP:
    # Central directory file header signature = 0x02014b50
    HEADER_SIGNATURE = slice(0, 4)
    # Version made by
    VERSION_MADE_BY = slice(4, 6)
    # Version needed to extract (minimum)
    EXTRACT_VERSION = slice(6, 2)
    # General purpose bit flag
    BIT_FLAG = slice(8,10)
    # Compression method
    COMPRESSION_METHOD = slice(10,12)
    # File last modification time
    LAST_MODIFICATION_TIME = slice(12,14)
    # File last modification date
    LAST_MODIFICATION_DATE = slice(14,16)
    # CRC-32
    CRC_32 = slice(16,20)
    # Compressed size
    COMPRESSED_SIZE = slice(20,24)
    # Uncompressed size
    UNCOMPRESSED_SIZE = slice(24,28)
    # File name length (n)
    FILE_NAME_LENGTH = slice(28,2)
    # Extra field length (m)
    EXTRA_FIELD_LENGTH = slice(30,32)
    # File comment length (k)
    FILE_COMMENT_LENGTH = slice(32,34)
    # Disk number where file starts
    FILE_WHERE_START_IN_DISK = slice(34,36)
    # Internal file attributes
    INTERNAL_ATTRIBUTES = slice(36,38)
    # External file attributes
    EXTERNAL_ATTRIBUTES = slice(38,42)
    # relative offset of local header
    RELATIVE_OFFSET_OF_LOCAL_HEADER = slice(42,46)
    # File name
    FILE_NAME = slice(46,int.from_bytes(FILE_NAME_LENGTH,byteorder='big'))
    # Extra field
    EXTRA_FIELD = slice(46+int.from_bytes(FILE_NAME_LENGTH,byteorder='big'),
                        46+int.from_bytes(FILE_NAME_LENGTH,byteorder='big')
                        +int.from_bytes(EXTRA_FIELD_LENGTH,byteorder='big'))
    # File comment
    FILE_COMMENT = slice(46+int.from_bytes(FILE_NAME_LENGTH,byteorder='big')
                        +int.from_bytes(EXTRA_FIELD_LENGTH,byteorder='big'),
                         46+int.from_bytes(FILE_NAME_LENGTH,byteorder='big')
                        +int.from_bytes(EXTRA_FIELD_LENGTH,byteorder='big')+
                         int.from_bytes(FILE_COMMENT_LENGTH,byteorder='big'))

    def __init__(self,data):
        self.data = data


    def set(self,attribute,data:bytes):
        self.data[attribute] = data

    def get(self,attribute):
        return self.data[attribute]
