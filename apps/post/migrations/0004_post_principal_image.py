# Generated by Django 4.2.6 on 2023-10-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_images_post_images_related'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='principal_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Principal Image'),
        ),
    ]
