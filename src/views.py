from aiohttp import web

async def index(request):
    return web.Response(text="Hello World")

async def queue(request):
    return web.Request(text="This is where the queue goes.")

