from django.urls import path
from .views import booksView, bookPreview_view, update_book_view, get_book, delete_book_view, search_books_view, filter_books_by_category, filter_books_by_author

urlpatterns = [
    path('add-book',booksView, name='addBooks'),
    path('search_books/', search_books_view, name='search_books'),
    path('filter_books_by_category/', filter_books_by_category, name='filter_books_by_category'), 
    path('filter_books_by_author/', filter_books_by_author, name='filter_books_by_author'),
    path('',bookPreview_view,name='booksPreview'),
    path('get-book/<str:book_id>/', get_book, name="get_book"),
    path('update-book',update_book_view,name='updateBook'),
    path('delete-book',delete_book_view,name='deleteBook'),
]
