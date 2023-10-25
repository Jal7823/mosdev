# Generated by Django 4.2.6 on 2023-10-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='publicity', verbose_name='Image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]