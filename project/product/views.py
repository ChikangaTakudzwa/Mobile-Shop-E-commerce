from django.shortcuts import render
from product.models import Product

# Create your views here.
def product(request, model):
    products = Product.objects.filter(model=model)
    context = {
        "item": products
    }
    
    return render(request, "product/product.html", context)