from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import select_template

from app.internal.models.post import Post


def index(request):
    return HttpResponse(render(request, "index.html"))


def blog(request):
    context = {"post_list": Post.objects.all()}
    return HttpResponse(render(request, "blog.html", context))


def get_post(request, post_name):
    template = select_template([f"{post_name}.html", 'post_not_found.html'])

    return HttpResponse(template.render())
