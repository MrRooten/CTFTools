import hashlib

def ntlm(string:str):
    return hashlib.new('md4',string.encode('utf-16le'))

def md5(string:str):
    return hashlib.new('md5',string.encode())

