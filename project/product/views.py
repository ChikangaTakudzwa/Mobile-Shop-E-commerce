from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, Review

# Create your views here.
def product(request, model):
    products = get_object_or_404(Product, model=model)

    if request.method == 'POST':
        rating = request.POST.get('review', 3)
        content = request.POST.get('message', '')

        if content:
            review = Review.objects.create(
                product=products,
                rating=rating,
                content=content,
                created_by=request.user
            )
            return redirect('product', model=model)

    context = {
        "items": products
    }
    
    return render(request, "product/product.html", context)