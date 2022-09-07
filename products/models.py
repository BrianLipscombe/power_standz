from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    A model for product reviews.
    """
    product = models.ForeignKey(
        'Product', null=True, blank=True,
        related_name='reviews', on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(
        null=False, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    review = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ", " + str(self.product)