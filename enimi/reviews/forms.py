from django import forms

from reviews.models.reviews import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rate_choices']
        widgets = {
            'text': forms.TextInput(attrs={"class": "review__box", "placeholder": "Добавить отзыв"})
        }
