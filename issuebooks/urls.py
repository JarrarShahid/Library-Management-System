from django.urls import path
from .views import return_issue_book_view, get_issue_invoice, issue_a_book, search_issued_books, issue_books_preview

urlpatterns = [
    path('issue-book/',issue_a_book,name="issueBook"),
    path('return-book/',return_issue_book_view, name='returnBook'),
    path('get-issue-book/<str:issue_ID>/',get_issue_invoice, name='getIssueBook'),
    path('issued-books-preview/',issue_books_preview,name="issueBooksPreview"),
    path("search_issued_books/", search_issued_books, name="search_issued_books"),
]