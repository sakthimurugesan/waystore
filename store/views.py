from django.shortcuts import render, redirect
from django.http import request
from .models import *


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
    context = {
        'product': Product.objects.get(product_slug=product_slug)
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