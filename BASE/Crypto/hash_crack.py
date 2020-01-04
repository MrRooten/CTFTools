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
        "algorithm":None,
        "start":None,
        "end":None,
        "target":None
    }

    def run(self):
        try:
            print(self.__options__)
            hash_algorithm = self.__options__["algorithm"]
            exec("from hashlib import "+hash_algorithm)
            module = eval(hash_algorithm)
            start = int(self.__options__["start"])
            end = int(self.__options__["end"])
            target = self.__options__["target"]
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

