import bleach
from django.db import models
from django.utils.safestring import mark_safe


class Brands(models.Model):
    brand_name = models.CharField(max_length=250, unique=True)
    brand_slug = models.CharField(max_length=300, unique=True)
    brand_image = models.ImageField(upload_to='brand_image/')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = "Brands"
        verbose_name_plural = "Brands"


class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    category_slug = models.CharField(max_length=500, unique=True)
    category_image = models.ImageField(upload_to='category_images/')

    recently_add = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)

    sub_category = models.ForeignKey(to="self", on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    def count(self, brand_name):
        return len(Brands.objects.filter(brand_name=brand_name))


class Product(models.Model):
    product_name = models.CharField(max_length=500, unique=True)
    product_slug = models.CharField(max_length=500, unique=True)
    product_card_image = models.ImageField(unique='product_card_image/')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_short_description = models.TextField(blank=True, null=True, default="Not more than 40 words",
                                                 help_text="Not more than 40 words")
    product_highlights = models.TextField(blank=True, null=True, default="Highlight three points",
                                          help_text="Highlight three points")

    recently_add = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    popular_in_category = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    selling_price = models.DecimalField(max_length=25, max_digits=25, decimal_places=3)
    actual_price = models.DecimalField(max_length=25, max_digits=25, decimal_places=3, blank=True, null=True)
    stock = models.IntegerField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_rendered_description(self):
        cleaned_description = bleach.clean(self.product_description)
        return mark_safe(cleaned_description)

    def __str__(self):
        return self.product_name


class GalleryImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to='gallery_image/',blank=True,null=True)
