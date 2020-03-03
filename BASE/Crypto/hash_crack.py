import sys
import importlib
from lib.baseClass import BaseModule

class Module(BaseModule):
    __info__ = {"Author":"Sam0ple",
                "Arugment":"""
                start -> start of hash
                end -> end of hash
                algorithm -> hash algorithm
                target -> need hash[start:end] == target
                """,
                "Descript":"crack hash algorithm"
                }
    __options__ = {
        "algorithm":{"args":"","necessity":True,"description":"hash algorithm"},
        "start":{"args":"","necessity":True,"description":"start index of hash"},
        "end":{"args":"","necessity":True,"description":"end index of hash"},
        "target":{"args":"","necessity":True,"description":"need hash[start:end]==target"}
    }

    def run(self):
        try:
            print(self.__options__)
            hash_algorithm = self.__options__["algorithm"]["args"]
            exec("from hashlib import "+hash_algorithm)
            module = eval(hash_algorithm)
            start = int(self.__options__["start"]["args"])
            end = int(self.__options__["end"]["args"])
            target = self.__options__["target"]["args"]
            i = 0
            while True:
                if i % 100000 == 0:
                    print("\rprocess {}".format(i),end='')
                    sys.stdout.flush()
                if module(str(i).encode()).hexdigest()[start:end] == target:
                    print("Result {}".format(str(i)))
                    break
                i = i+1



        except Exception as e:
            print("[Error] {}".format(e))

