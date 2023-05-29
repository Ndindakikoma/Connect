from django.shortcuts import render
from . import templates

def homepage(request):
    return render(request, 'base/index.html')
