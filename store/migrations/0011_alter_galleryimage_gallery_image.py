# Generated by Django 5.0.1 on 2024-01-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_galleryimage_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='gallery_image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_image/'),
        ),
    ]