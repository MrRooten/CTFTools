from lib.baseClass import BaseModule
from lib.toolutils.pathtool import platform_path
import re
import os
class Module(BaseModule):
    __options__ = {"regex":{"args":"","necessity":True,"description":"use for filter"}}
    __info__ =  {"Author":"Sam0ple","description":"use regex to filter the xss vectors"}
    def run(self):
        try:
            xss_vectors = []
            for i in os.listdir(platform_path("SecLists$Fuzzing$XSS$")):
                xss_vectors += open(platform_path("SecLists$Fuzzing$XSS$")+i).read().split("\n")
            valids = []
            for i in xss_vectors:
                regex = re.compile(self.__options__["regex"]["args"])
                if not regex.match(i):
                    valids.append(i)
                    print(i)
            return valids
        except Exception as e:
            print(e)
