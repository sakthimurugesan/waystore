from django.contrib import admin
from django.utils.html import format_html

from .models import CustomUser
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('profile_photo')
class UserAdmin(admin.ModelAdmin):
    def image_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="max-height: 70px; max-width: 70px;" />', obj.profile_photo.url)
        else:
            return "No photo"

    image_preview.short_description = 'Image Preview'

    list_display = ['email', 'image_preview']
    exclude = ['password', 'last_login']

admin.site.register(CustomUser, UserAdmin)

