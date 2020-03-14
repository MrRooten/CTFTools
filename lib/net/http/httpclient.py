import aiohttp
import requests
import asyncio

import pdb
class HtppClientSync:
    hosts = []
    def __init__(self):
        pass

    def appendHost(self,host):
        self.hosts.append(host)

    def send(self,host):
        pass

    def sendall(self):
        pass

class HttpClientAsync:
    def __init__(self,urls,method="get",headers={},data=b"",params=b"",ssl=False):
        self.loop = asyncio.get_event_loop()
        self.urls = urls
        self.optional = {
            "method":method,
            "headers":headers,
            "data":data,
            "params":params
        }
        self.results = {}
        self.hosts = []
        self.ssl = ssl

    def appendHost(self,host):
        self.hosts.append(host)

    async def _sendall(self,handler):
        async with aiohttp.ClientSession() as session:
            try:
                headers = self.optional["headers"]
                res = None
                self.count = 0
                self.text = None
                for i in self.urls:
                    if self.optional["method"].lower() == "get":
                        async with session.get(i,params=self.optional["params"],headers=headers,ssl=self.ssl) as response:
                            self.results[i] = response
                            res = response
                            self.text = await res.text()
                    elif self.optional["method"].lower() == "post":
                        async with session.post(i,data=self.optional["data"],headers=headers,ssl=self.ssl) as response:
                            self.results[i] = response
                            res = response
                            self.text = await res.text()
                    elif self.optional["method"].lower() == "head":
                        async with session.head(i,headers=headers,ssl=self.ssl) as response:
                            self.results[i] = response
                            res = response
                            self.text = await res.text()
                    elif self.optional["method"].lower() == "put":
                        async with session.put(i,headers=headers,data=self.optional["data"],ssl=self.ssl) as response:
                            self.results[i] = response
                            res = response
                            self.text = await res.text()
                    elif self.optional["method"].lower() == "delete":
                        async with session.delete(i,headers=headers,ssl=self.ssl) as response:
                            self.results[i] = response
                            res = response
                            self.text = await res.text()
                    elif self.optional["method"].lower() == "options":
                        async with session.options(i,headers=headers):
                            self.results[i] = response
                            res = response
                            self.text = res.text()
                    self.count += 1

                    handler(res,self.count,self.text)
            except Exception as e:
                from lib.utils import print_error
                print_error(e)

    def sendall(self,func):
        self.loop.run_until_complete(self._sendall(func))

