from django.contrib import admin

from app.internal.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
