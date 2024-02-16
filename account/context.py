# myapp/context_processors.py
from requests import session

from store.models import Category,Brands
from account.models import CustomUser
from orders_cart_wishlist.models import Cart,Wishlist
def custom_context(request):
    request.session.save()
    name=""
    try:
        name=CustomUser.objects.get(id=request.user.id).first_name
    except:
        pass
    # Your context data goes here
    return {'brands': Brands.objects.all(),
            'categorys':Category.objects.all()
             ,'name':name
    }

def getuser(request):
    request.session.save()
    return {
        'email':request.session.get('email',None)
    }

def get_len_cart(request):
    if request.user.id is not None:
        return {
            'cart_len':Cart.objects.filter(user_id=request.user.id).__len__(),
            'wish_len':Wishlist.objects.filter(user_id=request.user.id).__len__(),
        }
    else:
        return {
            "":""
        }

