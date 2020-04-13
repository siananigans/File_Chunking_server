from aiohttp import web
import aiohttp_jinja2
import requests
import jinja2
import aiohttp
import aiofiles
import time

j = 0

@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    return

async def upload_file(request):
    start_time = time.time()

    global j
    if j == 50:
        j = 0
    j += 1
    print('In the post')


    reader = await request.multipart()


    field = await reader.next()
    first = await field.read_chunk()
    first = first.decode('utf-8')

    field = await reader.next()
    last = await field.read_chunk()
    last = last.decode('utf-8')


    field = await reader.next()



    content = ''
    url = "http://0.0.0.0/"

    #url = 'http://FileChunker-env.eba-3brp9tyy.eu-west-1.elasticbeanstalk.com/'


    end_data = {}

    while True:
        chunk = await field.read_chunk()
        if not chunk:
            break
        try:
            chunk = chunk.decode('utf-8', errors='ignore')
        except:
            chunk = chunk.decode()

        f = {'data': chunk,
             'first': first,
             'last': last
             }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=f) as resp:
                print(resp.status)
                j_data = await resp.json()
                end_data.update(j_data)


    lines = form_file(end_data)

    async with aiofiles.open('user_files/output-' + str(j), 'w+') as out:
        await out.write(str(lines))


    print(time.time() - start_time)
    return web.FileResponse('user_files/output-' + str(j))




async def queue_handler(request):
    return web.Response(text="This is where the queue goes.")



def form_file(dict):

    i = 0
    lines = ''
    ks = dict.keys()
    ks = list(ks)
    ks.sort()
    while i < len(ks):

        line = str(i) + '\t' + ks[i] + '\t' + ks[i] + '\t' + str(dict[ks[i]]) + '\n'
        lines += line
        i += 1

    return(lines)

