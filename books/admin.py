from django.contrib import admin
from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    # List Display: Muestra los atributos del objeto en forma de lista.
    list_display = (
        'title', 
        'isbn',
        'creation_date',
        'pages',
        )

    # Muestra un filtro para todos los objetos.
    list_filter = ('title', 'isbn',)

    # Abre un campo "search" para poder buscar por los campos indicados.
    search_fields = (
        'title', 
        'editorial',
        'isbn',
    )





# Debo registrarlo junto con el modelo referido.
admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):

    # List Display: Muestra los atributos del objeto en forma de lista.
    list_display = (
        'full_name', 
        'age',
        'is_active',
        'country_birth',
        'created_at',
        'book',
        )

    # Muestra un filtro para todos los objetos.
    list_filter = ['full_name', 'age', 'country_birth']

    # Abre un campo "search" para poder buscar por los campos indicados.
    search_fields = ['country_birth']


# Author
admin.site.register(Author, AuthorAdmin)