from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    content = RichTextField('Content', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField("Created",auto_now_add=True)
    update_at = models.DateField("Updated",auto_now=True)

    def __str__(self):
        return f'{self.author} / {self.title} '
