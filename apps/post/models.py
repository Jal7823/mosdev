from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from apps.categories.models import Categorie



class Images(models.Model):
    name = models.ImageField('Images', upload_to='media/multi_images')


class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    content = RichTextField('Content', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categorie, related_name='Categories')
    principal_image = models.ImageField('Principal Image', null=True, blank=True, upload_to='media/principal_images')
    images_related = models.ManyToManyField(Images, null=True, blank=True)
    created_at = models.DateField("Created", auto_now_add=True)
    update_at = models.DateField("Updated", auto_now=True)

    def __str__(self):
        return f'{self.author} / {self.title} '
