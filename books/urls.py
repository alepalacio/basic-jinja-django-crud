from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list-books'),

    path('create_book/', views.create_book, name='create-book'),
    
    path('update_book/<int:book_id>/', views.update_book, name='update-book'),

    path('delete_book/<int:book_id>/', views.delete_book, name='delete-book'),

    path('delete_ok/', views.delete_ok, name='delete-ok'),

    path('retrieve_book/<int:book_id>/', views.retrieve_book, name='retrieve-book')
]