from ctypes import *
def print_options(options:dict):
    for i in options.keys():
        print("{}:{}".format(i,options[i]))


def print_info(info:dict):
    for i in info.keys():
        print("{}:{}".format(i,info[i]))

def print_error(msg:str):
    print("[Error]:",msg)

def print_warning(msg:str):
    print("[Warning]:",msg)

def print_info(msg:str):
    print("[Info]:",msg)

def strArrayToPointer(strArray:list):
    res = (c_char_p)*(len(strArray))()
    for i in range(len(strArray)):
        res[i] = c_char_p(i)

    return res
