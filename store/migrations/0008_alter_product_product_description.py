# Generated by Django 5.0.1 on 2024-01-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
