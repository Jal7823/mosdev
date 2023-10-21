from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Categorie(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name
    
class Images(models.Model):
    images = models.ImageField('Images')
    

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    content = RichTextField('Content', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categorie,related_name='Categories')
    principal_image = models.ImageField('Principal Image',null=True, blank=True)
    images_related = models.ManyToManyField(Images)
    created_at = models.DateField("Created", auto_now_add=True)
    update_at = models.DateField("Updated", auto_now=True)

    def __str__(self):
        return f'{self.author} / {self.title} '
