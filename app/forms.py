# forms.py
from django import forms
from .models import News, Category, Author, Publisher


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'category', 'author', 'publishers']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select())
    publishers = forms.ModelMultipleChoiceField(queryset=Publisher.objects.all(), widget=forms.SelectMultiple())
