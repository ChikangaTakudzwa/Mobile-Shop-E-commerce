from django.shortcuts import render, get_object_or_404
from product.models import Product

# Create your views here.
def product(request, model):
    products = get_object_or_404(Product, model=model)
    
    context = {
        "items": products
    }
    
    return render(request, "product/product.html", context)