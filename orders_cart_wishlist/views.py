import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from account.models import CustomUser
from store.models import Product
from orders_cart_wishlist.models import Wishlist, Cart


# Create your views here.
def addtowishlist(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_page")
    if request.method=='GET':
        user_in_wishlist=None
        try:
            user_in_wishlist=Wishlist.objects.get(
                product_id=int(pid),
                user=request.user)
        except:
            pass
        print(user_in_wishlist==None)
        if user_in_wishlist is not None:
            user_in_wishlist.delete()
            messages.success(request,'Removed from wishlist')
        else:
            Wishlist.objects.create(
                product_id=int(pid),
                user=request.user)
            messages.success(request, 'Added to wishlist')
    return redirect(request.META.get('HTTP_REFERER'))




def addtocart(request, pid):
    if not request.user.is_authenticated:
        return redirect("login_page")
    if request.method == 'POST':
        try:
            user_status_in_cart = Cart.objects.get(
                product_id=int(pid),
                user=request.user
            )
        except:
            user_status_in_cart = None
        # print(user_status_in_cart)

        if user_status_in_cart is not None:
            if user_status_in_cart.quantity == Product.objects.get(id=pid).max_quantity:
                messages.success(request, "Maximum purchase limit reached")
            elif user_status_in_cart.quantity + int(request.POST['quantity']) <= Product.objects.get(
                    id=pid).max_quantity:
                user_status_in_cart.quantity = user_status_in_cart.quantity + int(request.POST['quantity'])
                user_status_in_cart.save()
                messages.success(request, "Product Added to Cart")
            else:
                user_status_in_cart.quantity = Product.objects.get(id=pid).max_quantity
                user_status_in_cart.save()
                messages.success(request, "Product Added to Cart")

        else:
            Cart.objects.create(
                product_id=int(pid),
                user=request.user,
                quantity=int(request.POST['quantity'])
            )
            messages.success(request, "Product Added to Cart")

    return redirect(request.META.get('HTTP_REFERER'))

def cart(request):
    if not request.user.is_authenticated:
        return redirect("login_page")
    c = Cart.objects.filter(
        user=request.user
    )
    total=0
    actual_total=0
    for i in c:
        total+=(i.quantity*i.product.selling_price)
        actual_total += (i.quantity * i.product.actual_price)
    context={
        "user_status_in_cart" : Cart.objects.filter(
        user=request.user
    ),'cart_total':total,'actual_total':actual_total,'discount':actual_total-total
    }


    return render(request,'cart/page-shopping-cart.html',context=context)

def wishlist(request):
    if not request.user.is_authenticated:
        return redirect("login_page")
    context={
        "user_status_in_cart" : Wishlist.objects.filter(
        user=request.user
    )
    }


    return render(request,'cart/page-shopping-wishlist.html',context=context)

def remove_from_cart(request,pid):
    if not request.user.is_authenticated:
        return redirect("login_page")

    user_in_cart=Cart.objects.get(
        user=request.user,
        product_id=int(pid)
    )
    user_in_cart.delete()
    return redirect("cart")
