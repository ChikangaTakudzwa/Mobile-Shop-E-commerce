from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()[0:8]
    context = {
        "products": products
    }
    return render(request, 'home/home.html', context)