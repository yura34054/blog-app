from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request, "index.html"))


def blog(request):
    return HttpResponse(render(request, "blog.html"))
