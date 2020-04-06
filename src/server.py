from aiohttp import web
from views import index


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)



async def my_web_app():
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    return app

if __name__ == '__main__':
    my_web_app()
