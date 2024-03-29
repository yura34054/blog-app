from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import select_template

from app.internal.models.post import Post


def index(request):
    return HttpResponse(render(request, "index.html"))


def blog(request):
    return HttpResponse(render(request, "blog.html"))


def get_post(request, post_slug):
    template = select_template([f"posts/{post_slug}.html", "post_not_found.html"])
    context = {"post_info": Post.objects.filter(slug=post_slug).first()}

    return HttpResponse(template.render(context))
