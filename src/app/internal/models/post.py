from django.db import models


class Post(models.Model):
    title = models.fields.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
