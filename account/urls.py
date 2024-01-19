from accounts.views import *
from django.urls import path
urlpatterns=[
    path('',views.home,name='store')
]