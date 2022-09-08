from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = Review
        exclude = (
            'user',
            'date_added',
            'product',
            'upvotes',
            'downvotes')

        fields = ['title', 'description', 'rating']

        labels = {
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = (
                'add-blog-form-field')