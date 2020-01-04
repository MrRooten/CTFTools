from lib.baseClass import BaseModule
import zlib
from itsdangerous import base64_decode
from flask.sessions import SecureCookieSessionInterface
import ast
class MockApp(object):
    def __init__(self,secret_key):
        self.secret_key = secret_key

def decode(session_cookie_value,secret_key=None):
    try:
        if secret_key == None:
            compressed = False
            payload = session_cookie_value

            if payload.startswith('.'):
                compressed = True
                payload = payload[1:]

            data = payload.split(".")[0]

            data = base64_decode(data)
            if compressed:
                data = zlib.decompress(data)

            return data
        else:
            app = MockApp(secret_key)

            si = SecureCookieSessionInterface()
            s = si.get_signing_serializer(app)

            return s.loads(session_cookie_value)
    except Exception as e:
        return "[Decoding error] {}".format(e)
        raise e



def encode(secret_key,session_cookie_structure):
    try:
        app = MockApp(secret_key)

        session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
        si = SecureCookieSessionInterface()
        s = si.get_signing_serializer(app)

        return s.dumps(session_cookie_structure)
    except Exception as e:
        return "[Encodeing error] {}".format(e)
        raise e
class Module(BaseModule):
    __info__ = {"Author":"Wilson Sumanang, Alexandre ZANNI",
                "github.com":"https://github.com/noraj/flask-session-cookie-manager",
                "Descript":"This module is for encoding and decoding flask session",
                "Arugments":"""
                flask_cookie -> string of flask cookie
                mode -> choice encode or decode
                string -> string to encode
                key -> encoding key
                """}
    __options__ = {"flask_cookie":None,"mode":"decode","string":None,"key":None}

    __result__ = {"decode":None,"encode":None}

    def run(self):
        if self.__options__["mode"] == "decode":
            if self.__result__["decode"] == None:
                self.__result__["decode"] = decode(self.__options__["flask_cookie"],self.__options__["key"])
                print("Decode Result:",self.__result__["decode"])
            else:
                print("Decode Result:",self.__result__["decode"])

        elif self.__options__["mode"] == "encode":
            if self.__result__["encode"] == None:
                self.__result__["encode"] = encode(self.__options__["string"],self.__options__["key"])
                print("Encode Result:",self.__result__)

            else:
                print("Encode Result:",self.__result__["encode"])


if __name__ == '__main__':
    pass