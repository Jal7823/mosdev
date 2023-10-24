# Generated by Django 4.2.6 on 2023-10-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_principal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='images',
            field=models.ImageField(upload_to='multi_images', verbose_name='Images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='images_related',
            field=models.ManyToManyField(blank=True, null=True, to='post.images'),
        ),
    ]
