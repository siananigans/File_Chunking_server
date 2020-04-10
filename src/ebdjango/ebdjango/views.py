import pickle
from django.shortcuts import render
from django.http import HttpResponse

def file_handler(request):
    if request.method == 'POST':
        # Chunk text
        #return 'postin'
        #data = request.POST['data']

        return HttpResponse(request)

    else:
        print('test ok')

def index_view(request):
    #print('Get request')
    return render(request, 'index.html')
