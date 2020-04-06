from src.views import index

def routes(app):
    app.router.add_get('/', index)