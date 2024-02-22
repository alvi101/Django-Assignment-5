from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["body"]
        labels = {
            "body": "Add a review",
        }
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }
