from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is my HOME!')

def group_posts(request, pk):
    return HttpResponse(f'Posts from Group {pk}')