from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, World!")
    #return render(request, 'main/base.html')
    return render(request, 'main/index.html')