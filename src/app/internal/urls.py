from django.urls import path

from app.internal.transport import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("blog/<str:post_slug>", views.get_post),
]
