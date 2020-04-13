from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
import re
from django.http import HttpResponse

def file_handler(request):
    if request.method == 'POST':
        # Chunk text

        d = request.POST.getlist('data')
        f = request.POST.getlist('first')
        l = request.POST.getlist('last')

        d = d[0]
        f = f[0]
        l = l[0]

        dict = chunk(str(d), str(f), str(l))


        #return HttpResponse(str(f))
        return JsonResponse(dict)

    else:
        return render(request, 'index.html')

def index_view(request):
    return render(request, 'index.html')

def chunk(text, f, l):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    f_pos = 0
    l_pos = 25
    while i < len(alphabet):
        if alphabet[i] == f:
            f_pos = i
        if alphabet[i] == l:
            l_pos = i
        i += 1

    words = text.split()
    print(words)

    word_freq = defaultdict(int)
    for word in words:
        word = word.lower()
        j = 0
        while j < len(alphabet):
            if word[0] == alphabet[j]:
                word_pos = j
            j += 1

        if re.match(r"\b[^\d\W]+\b", word) and word_pos >= f_pos and word_pos <= l_pos:
            word_freq[word] += 1

    return word_freq
