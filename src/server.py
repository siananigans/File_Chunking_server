from aiohttp import web
from routes import myroutes


def my_web_app():
    app = web.Application()
    myroutes(app)
    web.run_app(app)

if __name__ == '__main__':
    my_web_app()


"""When already in use comes up:

https://stackoverflow.com/questions/34253779/tomcat-server-error-port-8080-already-in-use

Commands -

netstat -lnp | grep 8080
kill -9 process_id
"""