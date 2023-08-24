from django.urls import path

from app.internal.transport import views
from app.internal.transport import htmx_api

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("blog/<str:post_slug>", views.get_post),

    path("api/get_posts", htmx_api.get_posts),
]
