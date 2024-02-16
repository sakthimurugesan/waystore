from django import template

from orders_cart_wishlist.models import Cart

register=template.Library()

@register.filter(name="product_total")
def product_total(foo):
    return foo.quantity*foo.product.selling_price

@register.filter(name="isEmpty")
def isEmpty(foo):
    if foo.stock<=0:
        return True
    else:
        return False

@register.filter(name="notEmpty")
def notEmpty(foo):
    if foo.stock<=0:
        return False
    else:
        return True