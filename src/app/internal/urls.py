from django.urls import path

from app.internal.transport import views

urlpatterns = [
    path("", views.index),
    path("blog/", views.blog),
    path("blog/<str:post_name>", views.get_post),
]
