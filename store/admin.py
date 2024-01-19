from django.utils.html import format_html
from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "category_slug": ("category_name",)
    }
    list_display = ['category_name', 'category_slug', 'category_image']


@admin_thumbnails.thumbnail('gallery_image')
class GalleryImageAdmin(admin.TabularInline):
    model = GalleryImage
    extra = 1
    min_num = 3
    max_num = 7


@admin_thumbnails.thumbnail('product_card_image')
class ProductAdmin(SummernoteModelAdmin):
    prepopulated_fields = {
        "product_slug": ("product_name",)
    }

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.product_card_image.url)

    image_preview.short_description = 'Image Preview'

    list_display = [
        'product_name', 'image_preview', 'brand_name', 'category_name', 'selling_price', 'stock',
    ]

    summernote_fields = ('product_description', 'product_short_description', 'product_highlights')
    inlines = [GalleryImageAdmin]


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "brand_slug": ("brand_name",)
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brands, BrandAdmin)
