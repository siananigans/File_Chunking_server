from aiohttp import web
import aiohttp_jinja2
import requests
import jinja2
import aiohttp


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    return

async def upload_file(request):
    print('In the post')
    data = await request.post()

    doc = data['doc']

    filename = doc.filename

    doc_file = data['doc'].file

    content = doc_file.read()
    print(content)
    url = "http://filechunker-env.eba-3brp9tyy.eu-west-1.elasticbeanstalk.com/file_chunker/"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=content) as resp:
            print(resp.status)
            print(await resp.text())

    return web.Response(text="File uploaded")

async def queue_handler(request):
    return web.Response(text="This is where the queue goes.")


