from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from .algorithms import IssueBooks
from django.contrib import messages
# Create your views here.

def issue_a_book(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":
        memberID = request.POST.get("memberID")
        bookID = request.POST.get("bookID")
        expectedReturn = request.POST.get("expectedReturn")

        try:
            with open('issuebooks/issueBooks.json', 'r') as file:
                issued_books = json.load(file)
        except:
            messages.error(request, 'Error While loading Databse Try Again!')
            return redirect("issueBook")

        issue_book_class = IssueBooks()
        status = issue_book_class.issue_a_book(issue_book_list=issued_books,memberID=memberID, bookID=bookID,expectedReturn=expectedReturn)
        messages.info(request, status)
        return redirect("issueBooksPreview")

    return render(request, "issueTemplates/issueBook.html")




def return_issue_book_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":
        memberID = request.POST.get("memberID")
        bookID = request.POST.get("bookID")
        issueID = request.POST.get("issueID")

        try:
            with open('issuebooks/issueBooks.json', 'r') as file:
                issued_books = json.load(file)
        except:
            messages.error(request, 'Error While loading Databse Try Again!')
            return redirect("issueBook")
        issue_book_class = IssueBooks()
        status = issue_book_class.return_book(issue_book_list=issued_books,issue_book_ID=issueID,memberID=memberID,bookID=bookID)
        messages.info(request, status)
        return redirect("issueBooksPreview")
    return render(request,"issueTemplates/returnBook.html")

def get_issue_invoice(request, issue_ID):
    with open('issuebooks/issueBooks.json', 'r') as file:
        issued_books = json.load(file)
    # next() it returns the first match of condition 
    issue_invoice = next((invoice for invoice in issued_books if invoice["IssueBookID"].lower() == issue_ID.lower()), None)
    return JsonResponse(issue_invoice)


def issue_books_preview(request):
    if not request.session.get('username'):
        return redirect('custom_login')

    try:
        with open('issuebooks/issueBooks.json', 'r') as file:
            issued_books = json.load(file)
    except:
        messages.error(request, 'Error While loading Databse Try Again!')
        return redirect("issueBook")
    
    return render(request,"issueTemplates/issueBooksPreview.html",{"issued_books":json.dumps(issued_books)})

def search_issued_books(request):
    print('called')
    query = request.GET.get('query','').lower()
    try:
        with open('issuebooks/issueBooks.json', 'r') as file:
            issued_books = json.load(file)
    except:
        messages.error(request, 'Error While loading Databse Try Again!')
        return redirect("issueBook")
    
    filtered = [issued_invoice for issued_invoice in issued_books if query in issued_invoice["IssueBookID"].lower() ]
    return JsonResponse({"issued_books": filtered})
