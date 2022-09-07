from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def review_product(request, product_id):
    """ Review a Product """

    # Get Product object
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Get User Review for Product
        product_review = Review.objects.filter(
            product=product, user=request.user).first()
        # If Review exists
        if product_review:
            new_review = False
            # Instantiate ReviewForm from POST data and review object
            review_form = ReviewForm(request.POST, instance=product_review)
        else:
            new_review = True
            # Instantiate ReviewForm from POST data
            review_form = ReviewForm(request.POST)
        # If form is valid
        if review_form.is_valid():
            # If Review is new
            if new_review:
                # Create Review object
                review = review_form.save(commit=False)
                # Set Product
                review.product = product
                # Set User
                review.user = request.user
                # Save review
                review.save()
                # Get review offer if it exists and apply it to Reward
                review_offer = Offer.objects.filter(
                    description="Review").first()
                if review_offer:
                    # Get User Reward
                    reward = Reward.objects.filter(user=request.user).first()
                    # If Reward exists
                    if reward:
                        # Set discount
                        reward.discount = review_offer.discount
                        reward.save()
                        discount = round(review_offer.discount, 0)
                        rewardstr = f'Thanks for being a great customer - \
                            you have earned {discount}% \
                            off your next order!'
                    else:
                        # Create reward object
                        reward = Reward(
                            user=request.user,
                            discount=review_offer.discount)
                        reward.save()
                        rewardstr = ""
                # Success message
                messages.success(
                    request,
                    f'Review added for product: {product.friendly_name}.\
                    {rewardstr}',
                    extra_tags='admin'
                )
            else:
                # Update Review
                review_form.save()
                # Success messsage
                messages.success(
                    request,
                    f'Review updated for product: {product.friendly_name}.',
                    extra_tags='admin'
                )
            # Redirect to Product detial page
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            # If rating not set
            if not review_form['rating'].value():
                # Error message
                messages.error(
                    request,
                    'Error - please rate product to add review.',
                    extra_tags='admin'
                )
            else:
                # Error message
                messages.error(
                    request,
                    'Failed to add or edit review. Please check review form.',
                    extra_tags='admin'
                )

    else:
        # Get Review object
        product_review = Review.objects.filter(
            product=product, user=request.user).first()
        # If Review exists
        if product_review:
            # Instatiate ReviewForm from Review object
            review_form = ReviewForm(instance=product_review)
        else:
            # Instatiate blank ReviewForm
            review_form = ReviewForm
    from_profile = False
    # Get referer
    referer = (request.META.get('HTTP_REFERER', '/'))
    # Set from_profile if referred from Profile page
    if referer:
        rarray = referer.split('/')
        if rarray:
            rarray.reverse()
            if len(rarray) > 1:
                if rarray[1] == "profile":
                    from_profile = True
    # Get all Categories
    categories_all = Category.objects.all()
    # set semplate
    template = "products/review_product.html"
    # Set context
    context = {
        'product': product,
        'product_review': product_review,
        'review_form': review_form,
        'categories_all': categories_all,
        'from_profile': from_profile
    }
    # Render Product review page
    return render(request, template, context)


@login_required
def delete_review(request, product_id, user_id):
    """ Delete an existing Review """
    # Get Product object
    product = get_object_or_404(Product, pk=product_id)
    # Get User object
    user = get_object_or_404(User, pk=user_id)
    # Get Review object for Product and User
    review = get_object_or_404(Review, product=product, user=user)
    # If user is not a superuser
    if not request.user.is_superuser:
        # Error message
        messages.error(
            request,
            'Sorry, only store administrators can do that.',
            extra_tags='admin'
        )
        # Redirect to Product detail page
        return redirect(reverse('product_detail', args=[product.id]))
    # Delete Rdview
    review.delete()
    # Success message
    messages.success(
        request,
        f'User { user.username} review deleted for product: \
            {product.friendly_name}.',
        extra_tags='admin'
    )
    # Redirect to Product detail page
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def review_product_all(request):
    """
    Review all products - redirects user to view all products
    """
    # Redirect to all Products
    return redirect(reverse('products'))