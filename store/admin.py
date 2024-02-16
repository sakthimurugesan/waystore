from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
import admin_thumbnails
from .views import *

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

    def view_product(self, obj):
        url = reverse('product_detail_displaying', args=[obj.product_slug])
        return format_html('<a href="{}" class="button" target="_blank">View Product</a>', url)

    view_product.short_description = 'View Product'
    view_product.allow_tags = True


    image_preview.short_description = 'Image Preview'

    list_display = [
        'product_name','view_product', 'image_preview', 'brand_name', 'category_name', 'selling_price', 'stock',
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
