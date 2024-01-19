# Generated by Django 5.0.1 on 2024-01-17 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_highlights',
            field=models.TextField(blank=True, default='Highlight three points', help_text='Highlight three points', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_short_description',
            field=models.TextField(blank=True, default='Not more than 40 words', help_text='Not more than 40 words', null=True),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='gallery_image/<django.db.models.fields.related.ForeignKey>/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
