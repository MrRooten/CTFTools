import asyncio

class TCPServer:
    def __init__(self,host,handler):
        self.host = host
        self.handler = handler

    async def _run(self):
        self.server = await asyncio.start_server(self.handler,self.host[0],self.host[1])
        async with self.server:
            await self.server.serve_forever()

    def run(self):
        asyncio.run(self._run())