from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
import re
from django.http import HttpResponse

def file_handler(request):
    if request.method == 'POST':
        # Chunk text

        d = request.POST.getlist('data')

        d = d[0]

        dict = chunk(str(d))


        return JsonResponse(dict)

    else:
        return render(request, 'index.html')

def index_view(request):
    return render(request, 'index.html')

def chunk(text):

    words = text.split()

    word_freq = defaultdict(int)
    for word in words:
        word = word.lower()
        if re.match('(\w+)',word):
            word_freq[word] += 1

    return word_freq
