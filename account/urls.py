import account.views as views
from django.urls import path
import orders_cart_wishlist.views as orders
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login_page'),
    path("add_user/",views.add_user,name="add_user"),
    path("logout/",views.logout,name="logout"),
    path("addtocart/<int:pid>", orders.addtocart, name="addtocart"),
    path("addtowishlist/<int:pid>", orders.addtowishlist, name="addtowishlist"),
    path("remove_cart/<int:pid>",orders.remove_from_cart,name='remove_from_cart')
]