from django import template

from orders_cart_wishlist.models import Cart

register=template.Library()

@register.filter(name="product_total")
def product_total(foo):
    return foo.quantity*foo.product.selling_price

@register.filter(name="cart_total")
def cart_total(foo):
    total=0
    for i in foo:
        total+=(i.quantity*i.product.selling_price)