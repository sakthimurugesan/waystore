# Generated by Django 5.0.1 on 2024-01-16 16:52

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_brands_options_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]