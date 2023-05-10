from django import forms
from .models import Book


class BookForm(forms.Form):

    title = forms.CharField(label='Título')
    isbn = forms.IntegerField(label='ISBN')
    creation_date = forms.DateField(label='Fecha de creación')
    pages = forms.IntegerField(label='Páginas')
    editorial = forms.CharField(label='Editorial')