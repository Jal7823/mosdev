from django.db import models


class Publicity(models.Model):
    name = models.CharField('Name', max_length=100)
    url = models.ImageField('Image', upload_to='media/publicity')
    created_at = models.DateField('Created At', auto_now_add=True)
    updated_at = models.DateField('Updated At', auto_now=True)

    def __str__(self):
        return self.name
