import asyncio
import copy
from lib.utils import print_error
'''
This class is for handling mutiple target with tcp client 
'''
class TCPClientAsync(object):
    def __init__(self,dsts:list):
        self.dsts = copy.copy(dsts)

    async def _sendall(self,handler):
        try:
            for dst in self.dsts:
                reader,writer = await asyncio.open_connection(dst[0],dst[1])
                handler(reader,writer)
        except Exception as e:
            print_error(e)
        finally:
            if writer.is_closing():
                return
            else:
                writer.close()



    def sendall(self,handler):
        asyncio.run(self._sendall(handler))
    def appenddst(self,dst):
        self.dsts.append(dst)


