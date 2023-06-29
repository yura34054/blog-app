from django.db import models

THEME_CHOICES = [
    ("T", "Technology"),
    ("L", "Life"),
]


class Post(models.Model):
    title = models.fields.CharField(max_length=64, primary_key=True)
    slug = models.SlugField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=256)
    theme = models.CharField(
        max_length=1,
        choices=THEME_CHOICES,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
