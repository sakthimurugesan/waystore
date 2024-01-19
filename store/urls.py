import store.views as views
from django.urls import path
urlpatterns=[
    path('',views.store,name='store'),
    path("product/<str:product_slug>/", views.product_displaying_indetail, name='product_detail_displaying'),
    path("brand/", views.brand_displaying, name='brand_displaying'),
    path("brand/<str:brand>", views.brand_product_displaying, name="brand_product_displaying"),
    path("brand/<str:brand>/<str:product>",views.brand_product_detail_displaying,name='brand_product_detail_displaying'),
    path("category/",views.category_display,name="category_display"),
    path("category/<str:category>",views.category_product_displaying,name="category_product_displaying"),
path("category/<str:category>/<str:product>",views.category_product_detail_displaying,name='category_product_detail_displaying'),

]