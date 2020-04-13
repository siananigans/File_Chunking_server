from aiohttp import web
from views import index_handler, upload_file, queue_handler

def myroutes(app):

    app.add_routes([web.get('/', index_handler),
                    web.post('/', upload_file),
                    web.get('/queue', queue_handler)
                    ])

