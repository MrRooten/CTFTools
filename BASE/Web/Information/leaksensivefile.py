from lib.net.http.httpclient import HttpClientAsync
from lib.baseClass import BaseModule
from lib.toolutils.pathtool import platform_path
import sys

class Module(BaseModule):
    __info__ = {}
    __options__ = {"url":{"args":"","necessity":True,"description":"url of website"},
                   "suffix":{"args":"","necessity":False,"description":"suffix of wordlist like:php,jsp,html"},
                   "wordlist":{"args":"","necessity":False,"description":"wordlist"},
                   "notfound_identification":{"args":"","necessity":False,"description":"use regex to get not found page"},
                   "headers":{"args":"","necessity":False,"description":"headers of request"},
                   "ssl":{"args":"False","necessity":False,"description":"use ssl or not"},
                   "post":{"args":"","necessity":False,"description":"post data"}}

    def _getSuffixURL(self):
        if self.__options__["wordlist"]["args"] == "":
            wordlist = platform_path("SecLists$Discovery$Web-Content$common.txt")
        else:
            wordlist = self.__options__["wordlist"]["args"]

        url = ""
        if self.__options__["wordlist"]["args"].endswith("/"):
            url += self.__options__["url"]["args"]
        else:
            url += self.__options__["url"]["args"]+"/"
        urls = []
        with open(wordlist) as f:
            for file in f:
                for suffix in self.__options__["suffix"]["args"].split(","):
                    if self.__options__["suffix"]["args"] == "":
                        urls.append(url+file[:-1])
                    else:
                        urls.append(url+file[:-1]+"."+suffix)


        return urls
    def _get404Error(self):
        pass

    def handler(self,args,count):
        if args.status == 404:
            if count % 33 == 0:
                print("\rAlready scan:",count,end='')
                sys.stdout.flush()
            return
        else:
            print(args.url)
    def run(self):
        try:
            if self.__options__["notfound_identification"]["args"] == "":
                status = 404
            httpClient = HttpClientAsync(self._getSuffixURL(),data=self.__options__["post"]["args"],method="post")

            httpClient.sendall(self.handler)
        except Exception as e:
            print(e)