# Generated by Django 5.0.1 on 2024-01-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_product_highlights_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='gallery_image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery_image/<django.db.models.fields.related.ForeignKey>/'),
        ),
    ]