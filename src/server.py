from aiohttp import web
from routes import routes


async def my_web_app():
    app = web.Application()
    routes(app)
    return app

if __name__ == '__main__':
    my_web_app()
