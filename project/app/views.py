from django.shortcuts import render
from product.models import Product, Category
from django.conf import settings
from django.db.models import Q

# Create your views here.
def index(request):
    products = Product.objects.all()[0:8]
    category = Category.objects.all()
    active_category = request.GET.get('category', '')
    context = {
        "products": products,
        "categories": category,
        "ad": active_category
    }
    return render(request, 'home/home.html', context)

def shop(request):
    category = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(slug=active_category)

    query = request.GET.get('query', '')
    if query:
        # use Q to query many table columns
        products = products.filter(Q(name__contains=query) | Q(description__contains=query))
    context = {
        "products": products,
        "categories": category,
        "ad": active_category
    }
    return render(request, 'shop/shop.html', context)