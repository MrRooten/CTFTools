from lib.baseClass import BaseModule
from ctypes import *
class Module(BaseModule):
    __info__ = {"Author":"lepiaf",
                "github":"https://github.com/lepiaf/php_mt_seed",
                "options":"""
                args -> VALUE_OR_MATCH_MIN [MATCH_MAX [RANGE_MIN RANGE_MAX]] ...
                """}
    __options__ = {"args":{"args":"","necessity":True,"description":"VALUE_OR_MATCH_MIN [MATCH_MAX [RANGE_MIN RANGE_MAX]]"}}
    def run(self):
        pass

