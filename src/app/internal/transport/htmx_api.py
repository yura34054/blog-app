from django.http import HttpResponse
from django.shortcuts import render

from app.internal.models.post import Post


def get_posts(request):
    context = {"post_list": Post.objects.all()}
    return HttpResponse(render(request, "elements/post_list.html", context))
