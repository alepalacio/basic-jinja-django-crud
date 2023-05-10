from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=100)
    isbn = models.BigIntegerField()
    creation_date = models.DateField()
    pages = models.IntegerField()
    editorial = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Author(models.Model):

    full_name = models.CharField(max_length=50) # Caracteres / String
    age = models.IntegerField() # Números enteros
    is_active = models.BooleanField(default=True) # Datos booleanos True - False
    country_birth = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Nombre autor: {self.full_name}"

    

