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
    hosts = []
    def __init__(self,urls,method="get",headers={},data=b"",params=b""):
        self.loop = asyncio.get_event_loop()
        self.urls = urls
        self.optional = {
            "method":method,
            "headers":headers,
            "data":data,
            "params":params
        }
        self.results = {}

    def appendHost(self,host):
        self.hosts.append(host)

    async def _sendall(self,func):
        async with aiohttp.ClientSession() as session:
            headers = self.optional["headers"]
            res = None
            for i in self.urls:
                if self.optional["method"].lower() == "get":
                    async with session.get(i,params=self.optional["params"],headers=headers) as response:
                        self.results[i] = response
                        res = response
                elif self.optional["method"].lower() == "post":
                    async with session.post(i,data=self.optional["data"],headers=headers) as response:
                        self.results[i] = response
                        res = response
                elif self.optional["method"].lower() == "head":
                    async with session.head(i,headers=headers) as response:
                        self.results[i] = response
                        res = response
                elif self.optional["method"].lower() == "put":
                    async with session.put(i,headers=headers,data=self.optional["data"]) as response:
                        self.results[i] = response
                        res = response
                elif self.optional["method"].lower() == "delete":
                    async with session.delete(i,headers=headers) as response:
                        self.results[i] = response
                        res = response
                elif self.optional["method"].lower() == "options":
                    async with session.options(i,headers=headers):
                        self.results[i] = response
                        res = response

                func(res)

    def sendall(self,func):
        self.loop.run_until_complete(self._sendall(func))

