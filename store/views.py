from django.shortcuts import render, redirect
from django.http import request
from .models import *
import account.models as account
from orders_cart_wishlist.models import Cart,Wishlist

def store(request):
    context = {
        'product': Product.objects.all(),
        'category': Category.objects.all().order_by('category_name'),

    }
    return render(request, 'store/store.html', context=context)


def brand_displaying(request):
    context = {
        'brands': Brands.objects.all()
    }
    return render(request, 'store/brand_displaying.html', context=context)



def product_displaying_indetail(request, product_slug):
    wishlist = False
    quantity_in_cart = None
    try:
        cart_entry = Cart.objects.get(
            user=request.user,
            product=Product.objects.get(product_slug=product_slug)
        )
        quantity_in_cart = cart_entry.quantity

    except:
        quantity_in_cart = None

    print('-' * 50)
    try:
        wishlist = Wishlist.objects.filter(
            user=request.user,
            product=Product.objects.get(product_slug=product_slug)
        ).exists()
    except:
        pass



    user_email = request.session.get('user_email')
    context = {
        'product': Product.objects.get(product_slug=product_slug),
        'quantity_in_cart': quantity_in_cart,
        'wishlist': wishlist
    }

    return render(request, 'store/product_detail_displaying.html', context=context)


def brand_product_displaying(request,brand):
    products=Product.objects.filter(brand_name=Brands.objects.get(brand_slug=brand).id)
    context = {
        'product': Product.objects.filter(brand_name=Brands.objects.get(brand_slug=brand).id),
        'category': Category.objects.all().order_by('category_name'),
        "brand_name" : Brands.objects.get(brand_slug=brand).brand_name

    }


    return render(request,"store/brand_product_displaying.html",context=context)

def brand_product_detail_displaying(request,brand,product):
    context = {
        'product': Product.objects.get(product_slug=product)
    }
    return render(request, 'store/product_detail_displaying.html', context=context)

def category_display(request):
    context={
        'categories':Category.objects.all()
    }
    return render(request,"store/category_displaying.html",context=context)

def category_product_displaying(request,category):
    context={
        "products":    Product.objects.filter(category_name=Category.objects.get(category_slug=category).id),
        "category":Category.objects.get(category_slug=category).category_name
    }
    return render(request,"store/category_product_displaying.html",context)

def category_product_detail_displaying(request,category,product):
    context = {
        'product': Product.objects.get(product_slug=product)
    }
    return render(request, 'store/product_detail_displaying.html', context=context)

def add_to_cart(request,pid):
    pass

def brand_category_product_displaying(request,brand,category):
    context={
        'product':Product.objects.filter(brand=brand,category=category)
    }
    print(context)
    return redirect('/')