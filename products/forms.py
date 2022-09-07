from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    A form for Reviews.
    """
    class Meta:
        # Set model
        model = Review
        # Set field names
        fields = ('rating', 'review')
        # Set field labels
        labels = {
            'rating': 'Rating',
            'review': 'Review',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, set autofocus on review field
        """
        super().__init__(*args, **kwargs)
        # Set placeholders
        placeholders = {
            'rating': 'Rating',
            'review': 'Review',
        }
        # Set autofocus to review field
        self.fields['review'].widget.attrs['autofocus'] = True
        # Loop through fields, add placeholders
        for field_name, placeholder in placeholders.items():
            # Add a * to placeholder if field is required
            if self.fields[field_name].required:
                placeholder_text = placeholder + "*"
            else:
                placeholder_text = placeholder
            # Set placeholder
            self.fields[field_name].widget.attrs[
                'placeholder'] = placeholder_text
            # Add review-input class
            self.fields[field_name].widget.attrs[
                'class'] = 'review-input'