
from django.urls import path
import orders_cart_wishlist.views as views
urlpatterns=[
    path('cart/',views.cart,name='cart'),
    path('wishlist/',views.wishlist,name='wishlist')

]