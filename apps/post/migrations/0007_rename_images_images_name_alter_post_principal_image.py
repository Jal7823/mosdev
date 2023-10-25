# Generated by Django 4.2.6 on 2023-10-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_principal_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='images',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='principal_image',
            field=models.ImageField(blank=True, null=True, upload_to='principal_images', verbose_name='Principal Image'),
        ),
    ]