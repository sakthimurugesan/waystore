from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, request
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('store/', include('store.urls')),
path('summernote/', include('django_summernote.urls')),
]
