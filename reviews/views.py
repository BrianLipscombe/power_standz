from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Avg

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


def add_review(request, product_id):
    """
    Allow user to add a review and redirect them back to the
    item product item view
    """
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    review_details = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }
    review_form = ReviewForm(review_details)

    # If form is valid, add user and product and save
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.user = user
        review.product = product
        review.save()

        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.avg_rating = int(avg_rating)
        product.save()

        messages.success(request, 'Thank you! Your review was added')
    else:
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_detail', args=(product_id,)))


def edit_review(request, review_id):
    """
    Saves review form edited by user
    """
    review = get_object_or_404(Review, pk=review_id)
    review_form = ReviewForm(request.POST, instance=review)
    product = Product.objects.get(name=review.product)
    if review_form.is_valid():
        review.save()

        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.avg_rating = int(avg_rating)
        product.save()

        # Success message if added
        messages.success(request, 'Thank You! Your review was edited')
    else:
        # Error message if form was invalid
        messages.error(request, 'Something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_detail', args=(review.product.id,)))


def delete_review(request, review_id):
    """
    Deletes user's review
    """
    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.get(name=review.product)

    try:
        review.delete()

        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            product.avg_rating = int(avg_rating)
        else:
            product.avg_rating = 0

        product.save()
        messages.success(request, 'Your review was deleted')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" eroor:{e} occured. Try again later.")

    return redirect(reverse('product_detail', args=(review.product.id,)))
