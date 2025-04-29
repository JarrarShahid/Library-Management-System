from django.shortcuts import render, redirect
from .algorithms import Books
from datetime import datetime
from django.http import JsonResponse
from django.contrib import messages

import json
# Create your views here.
def booksView(request):
    if not request.session.get('username'):
        return redirect('custom_login')

    data = {}
    # with open('books.json','r') as booksFile:
    #     books = json.load(booksFile)
    if request.method == "POST":
        # initalizing error variables
        title_error = None
        author_error = None
        ageLimit_error = None
        copies_error = None

        # getting POST data from template
        title = request.POST.get('title')
        author = request.POST.get('author')
        categories = request.POST.get('categories').split(',')
        ageLimit = request.POST.get('ageLimit')
        copies = request.POST.get('copies')
        raw_releaseDate = request.POST.get('releaseDate')

        # formatting date to (month dd, yyyy)
        releaseDate = datetime.strptime(raw_releaseDate, "%Y-%m-%d").strftime("%B %d, %Y")

        data={
            'title': title,
            'author': author,
            'categories': json.dumps(categories),
            'ageLimit': ageLimit,
            'copies': copies,
            'releaseDate': raw_releaseDate

        }

        # validating title
        if not title:
            title_error = 'Please Enter Book Title'
        elif len(title) < 3:
            title_error = 'Title must be of 3 characters atleast!'
        elif any(char in title for char in ['@', '$', '#', '%', '&', '+','!']):
            title_error = 'No Special characters are allowed in Title except "-"'
        

        # validating Author
        if not author:
            author_error = 'Please Enter Author name'
        elif len(author) < 3:
            author_error = 'Author name must be of 3 characters atleast!'
        elif any(char in author for char in ['@', '$', '#', '%', '&', '+','!']):
            author_error = 'No Special characters are allowed except "-"'
        

        # validating Age Limit
        if not ageLimit:
            ageLimit_error = 'Please enter age limit'
        else:
            try:
                ageLimit_int = int(ageLimit)
            except ValueError:
                ageLimit_error = 'Age limit must be an integer value'
            
        
        # validating Number of copies
        if not copies:
            copies = 'Please enter number of copies'
        else:
            try:
                copies_int = int(copies)
            except ValueError:
                copies_error = 'Number of copies must be an integer value'
            
            
        

        # If any error exists rendering the same page with errors
        if title_error or author_error or ageLimit_error or copies_error:
            data.update({
                'error': True,
                'title_error': title_error,
                'author_error': author_error,
                'ageLimit_error': ageLimit_error,
                'copies_error': copies_error
            })
            return render(request, "addBooksPage.html",data)
        
        books_class = Books()
        
        try:
            with open('books/books.json','r') as file:
                books = json.load(file)
                print(books)
            
            try:
                status = books_class.add_a_book(bookList=books,title=title,author=author,category=categories,ageLimit=ageLimit, releaseDate=releaseDate,copies=copies)
                messages.info(request, status)
                return redirect("booksPreview")
            except:
                messages.error(request, "Can't add Book Something went Wrong try again")
                return redirect("addBooks")
            
        except FileExistsError:
            messages.error(request, "Book Database not found")
            return redirect("addBooks")

        
    return render(request, 'addBooksPage.html')



def bookPreview_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    with open('books/books.json','r') as booksFile:
        books = json.load(booksFile)
    # Extract authors and categories for filter options
    authors = list(set(book['author'] for book in books))
    categories = list(set(cat for book in books for cat in book['Category']))
    
    return render(request, "booksPreview.html", {
        "books": json.dumps(books),
        "authors": authors,
        "categories": categories,
    })
    # return render(request,"booksPreview.html",{"books":json.dumps(books)})

def search_books_view(request):
    query = request.GET.get('query', '').lower()  # Get the search query from URL params
    with open('books/books.json', 'r') as booksFile:
        books = json.load(booksFile)
    books_class = Books()
    
    filtered_books = books_class.dynamic_search_by_title_or_ID(bookList=books,query=query)

    # Return filtered books as a JSON response
    return JsonResponse({'books': filtered_books})


def filter_books_by_category(request):
    category = request.GET.get('category', '').lower()  # Get selected category

    with open('books/books.json', 'r') as booksFile:
        books = json.load(booksFile)

    books_class = Books()
   
    filtered_books = books_class.filter_by_category(bookList=books, category=category)

    return JsonResponse({'books': filtered_books})

def filter_books_by_author(request):
    author = request.GET.get('author', '').lower()  # Get selected author

    with open('books/books.json', 'r') as booksFile:
        books = json.load(booksFile)

    books_class = Books()

    filtered_books = books_class.filter_by_author(bookList=books,author=author)

    return JsonResponse({'books': filtered_books})




# For dynamically updating filling the form with details related to enterd book id
def get_book(request,book_id):
    try:
        with open('books/books.json', 'r') as file:
            books = json.load(file)
        
        books_class = Books()
        book_index = books_class.findBook(givenList=books,ID=book_id)
        print(book_index)
        if book_index is not None:
            # Convert "April 17, 2025" to "2025-04-17"
            try:
                release_date_obj = datetime.strptime(books[book_index]["releaseDate"], "%B %d, %Y")
                release_date_formatted = release_date_obj.strftime("%Y-%m-%d")
            except Exception:
                release_date_formatted = ''

            return JsonResponse({
                'title': books[book_index]["title"],
                'author': books[book_index]["author"],
                'category': json.dumps(books[book_index]["Category"]),
                'totalQTY': books[book_index]["totalQTY"],
                'ageLimit': books[book_index]["ageLimit"],
                'releaseDate': release_date_formatted
            })
    except FileNotFoundError:
        print('Error while reading books.json')


def update_book_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":
        books_class = Books()
        # getting data from template
        bookID = request.POST.get("bookID")
        title = request.POST.get("title")
        author = request.POST.get("author")
        categories = request.POST.get("categories").split(',')
        totalQTY = request.POST.get("totalQTY")
        ageLimit = request.POST.get("ageLimit")
        raw_releaseDate = request.POST.get("releaseDate")


        # formatting date to (month dd, yyyy)
        releaseDate = datetime.strptime(raw_releaseDate, "%Y-%m-%d").strftime("%B %d, %Y")

        try:
            with open('books/books.json', 'r') as file:
                books = json.load(file)
            
            status= books_class.update_book(bookList=books,bookID=bookID,title=title,author=author,category=categories,totalQTY=totalQTY,ageLimit=ageLimit,releaseDate=releaseDate)
            messages.info(request, status)
            return redirect("booksPreview")
        except Exception:
            messages.error(request, "Unable to Update Book Try again!")
            return  redirect("updateBook")

        # messages.error(request, "Session expired or email not found. Please register again.")

    return render(request,'updateBook.html')


def delete_book_view(request):
    if not request.session.get('username'):
        return redirect('custom_login')
    if request.method == "POST":
        books_class = Books()
        bookID = request.POST.get("bookID")

        try:
            with open('books/books.json', 'r') as file:
                books = json.load(file)
            
            status = books_class.delete_book(bookList=books, bookID=bookID)
            messages.success(request, status)
            return redirect("booksPreview")
            
        except Exception:
            messages.error(request, "Unable to Delete Book Try again!")
            return  redirect("deleteBook")

    return render(request,"deleteBook.html")