from django.contrib import admin
from .models import CustomUser


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    exclude = ['password','last_login']


admin.site.register(CustomUser, UserAdmin)
