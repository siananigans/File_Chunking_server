from aiohttp import web

async def index(request):
    print('IN the loop')
    return web.Response(text="Hello World")

async def queue(request):
    return web.Response(text="This is where the queue goes.")

