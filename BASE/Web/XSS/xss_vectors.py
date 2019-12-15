from lib.baseClass import BaseModule
from lib.toolutils.pathtool import platform_path
import re
class Module(BaseModule):
    __options__ = {"regex":""}
    __info__ =  {"Author":"Sam0ple","description":"use regex to filter the xss vectors"}
    def run(self):
        try:
            xss_vectors = open(platform_path("lib$xss_tools$xss_vectors.txt")).read().split("\n")
            valids = []
            for i in xss_vectors:
                regex = re.compile(self.__options__["regex"])
                if not regex.match(i):
                    valids.append(i)
                    print(i)
            return valids
        except Exception as e:
            print(e)
