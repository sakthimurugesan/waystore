# myapp/context_processors.py
from store.models import Category,Brands
def custom_context(request):
    # Your context data goes here
    return {'brands': Brands.objects.all(),
            'categorys':Category.objects.all()}
