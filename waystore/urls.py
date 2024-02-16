from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.http import HttpResponse, request
from django.shortcuts import render

from account.models import CustomUser
from waystore import settings


def home(request):
    request.session.save()
    print()
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('store/', include('store.urls')),
    path('account/', include('account.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('cart/', include('orders_cart_wishlist.urls')),
]
