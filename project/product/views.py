from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, Review

# Create your views here.
def product(request, model):

    products = get_object_or_404(Product, model=model)

    if request.method == 'POST':
        rating = request.POST.get('review', 3)
        content = request.POST.get('message', '')

        if content:

            # check to see if user already has a review in the database
            reviews = Review.objects.filter(created_by=request.user, product=products)

            # if review already exists for the user get the first one in the list
            # and update review with the values from the form
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content=content
                review.save()
            else:
                # else create new reveiw object
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