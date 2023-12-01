from django.db import models

class Categorie(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return f'{self.name}'