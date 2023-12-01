# Generated by Django 4.2.6 on 2023-11-30 17:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='media/multi_images', verbose_name='Images')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('principal_image', models.ImageField(blank=True, null=True, upload_to='media/principal_images', verbose_name='Principal Image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='Categories', to='categories.categorie')),
                ('images_related', models.ManyToManyField(blank=True, null=True, to='post.images')),
            ],
        ),
    ]
