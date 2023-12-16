import os
from django.shortcuts import render
from . import get_img

def main(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text', '')
        links = get_img.main(search_text)
        return render(request, 'images/main.html', {'search_text': search_text,
                                                    'links': links})

    return render(request, 'images/main.html')

