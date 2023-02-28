from django import forms
from . import models

class bookForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = '__all__'