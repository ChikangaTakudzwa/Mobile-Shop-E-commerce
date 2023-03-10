from django.shortcuts import render, redirect
from product.models import Product, Category
from django.conf import settings
from django.db.models import Q
from .forms import signUpForm, updateUserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from django.db.models import Sum

# Create your views here.
def index(request):
    products = Product.objects.all()[0:9]
    category = Category.objects.all()
    active_category = request.GET.get('category', '')
    context = {
        "products": products,
        "categories": category,
        "ad": active_category,
        "user": request.user
    }
    return render(request, 'home/home.html', context)

def signup(request):
    # check to see if user has clicked the submit button and run 
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # redirect the user to the index page
            return redirect('/')
    else:
        form = signUpForm()
    context = {
        "title": "Sign up",
        "form": form,
    }
    return render(request, 'auth/signup.html', context)


@login_required
def my_account(request):
    cart = Cart(request)
    product = Product.objects.all()
    orders = Order.objects.all()
    orditem = OrderItem.objects.all()
    # add all items in the prders queryset
    # total_order = orditem.aggregate(Sum('price'))['price__sum']
    context = {
        "user": request.user,
        "cart": cart,
        "product": product,
        "orders": orders,
        # "total_orderitem": total_order,
    }
    return render(request, 'auth/myaccount.html', context)


@login_required
def edit_my_account(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('me')
    return render(request, 'auth/myaccount.html')

def shop(request):
    category = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(slug=active_category)

    # get form data
    query = request.GET.get('query', '')
    if query:
        # use Q to query many table columns
        products = products.filter(Q(name__contains=query) | Q(description__contains=query))
    
    context = {
        "products": products,
        "categories": category,
        "ad": active_category,
    }
    return render(request, 'shop/shop.html', context)
    