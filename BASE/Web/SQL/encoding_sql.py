from lib.baseClass import BaseModule

class Module(BaseModule):
    __options__ = {"sql":{"args":"","necessity":True,"description":""},
                   "type":{"args":"","necessity":True,"description":"type of coding"}}
    __info__ = {"Author":"sam0ple",
                "arguments":"""
                sql -> need to be encoding
                type -> type of coding
                """}

    def charToDigit(self,sql:str):
        sql_chars = []
        for i in sql:
            sql_chars.append(str(ord(i)))

        sql_to_chars_function = "char(" + ','.join(sql_chars) + ')'  # char(*,*,*)
        return sql_to_chars_function
    def run(self):
        sql = self.__options__["sql"]["args"]
        if self.__options__["type"]["args"] == "charToDigit":
            print(self.charToDigit(sql))


