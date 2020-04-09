from views import index, queue


def myroutes(app):
    app.router.add_get('/', index)
    app.router.add_get('/queue', queue)