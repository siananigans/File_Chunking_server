from aiohttp import web
import aiohttp_jinja2
import requests
import jinja2
import aiohttp

j = 0

@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    return

@aiohttp_jinja2.template('download.html')
async def upload_file(request):

    global j
    j += 1
    print('In the post')
    reader = await request.multipart()

    field = await reader.next()

    content = ''
    url = "http://filechunker-env.eba-3brp9tyy.eu-west-1.elasticbeanstalk.com/"

    end_data = {}

    while True:
        chunk = await field.read_chunk()
        if not chunk:
            break
        chunk = chunk.decode('utf-8')
        f = {'data': chunk}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=f) as resp:
                print(resp.status)
                j_data = await resp.json()
                end_data.update(j_data)



    lines = format_file(end_data)

    with open('user_files/output-' + str(j), 'w+') as out:
        out.write(str(lines))

    """
    doc = data['doc']
    filename = doc.filename
    doc_file = data['doc'].file

    content = await doc_file.content.read()
    content = content.decode('utf-8')
    f = {'data': content}

    url = "http://filechunker-env.eba-3brp9tyy.eu-west-1.elasticbeanstalk.com/"
"""




async def queue_handler(request):
    return web.Response(text="This is where the queue goes.")

def format_file(dict):

    i = 0
    #line = "{}\t{}\t{}\t{}\n"
    lines = ''
    ks = dict.keys()
    ks = list(ks)
    ks.sort()
    while i < len(ks):

        line = str(i) + '\t' + ks[i] + '\t' + ks[i] + '\t' + str(dict[ks[i]]) + '\n'
        lines += line
        i += 1

    return(lines)

