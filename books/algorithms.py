import json
from datetime import datetime


    
class Books:
    def __init__(self):
        pass

    # Binary search for finding json through ID
    def findBook(self,givenList,ID):
        left, right = 0, len(givenList)-1

        while left <= right:
            midIndex = (left + right) // 2
            midValue =  givenList[midIndex]["BookID"][1:]
            if midValue == ID[1:]:
                return midIndex
            elif midValue< ID[1:]:
                left = midIndex +1
            else:
                right = midIndex -1
        
        return None
    
    # generate new book ID
    def generateBookID(self,bookList):
        # max ID is always last id because of sorted list
        maxID = int(bookList[-1]["BookID"][1:])
        
        if maxID:
            # add 1 in max Id to generate new ID in ascending order
            return f'B{maxID + 1:03d}'
        else:
            # generate first ID
            return f'B{1:03d}'
    
    # Checking if the given book is alraedy present or not
    def check_if_book_exists(self,bookList:list,title:str,author:str):
        for i,book in enumerate(bookList):
            if book["title"].lower() ==title.lower() and book["author"].lower() == author.lower():
                return i
        return None
    
    # Adding a new book
    def add_a_book(self,bookList:list,title:str,author:str,category:list,copies:int,ageLimit:int,releaseDate:str):
        # -----------------handling Duplicate Book Addition--------------------------------------------
        existing_book_index  = self.check_if_book_exists(bookList=bookList,title=title,author=author)



        if existing_book_index is not None:
            bookList[existing_book_index]["copies"] += int(copies)
 

            current_copies = bookList[existing_book_index]["copies"] 
            currently_issued = bookList[existing_book_index]["issuedQTY"] 

            # updating the total number of copies
            bookList[existing_book_index]["totalQTY"] = current_copies + currently_issued


            # Now write the updated list to json file
            with open('books/books.json','w') as booksFile:
                json.dump(bookList,booksFile,indent=4)
                return f"Quantity Added to Book ID {bookList[existing_book_index]["BookID"]}"
        #----------------------------------------------------------------------------------------------
        auto_generated_ID = self.generateBookID(bookList=bookList)

        bookList.append({
            "BookID": auto_generated_ID,
            "title": title,
            "author": author,
            "Category": category,
            "ageLimit": int(ageLimit),
            "releaseDate": releaseDate,
            "copies": int(copies),
            "addedDate": datetime.now().strftime("%B %d, %Y"),
            "issuedQTY": 0,
            "totalQTY": int(copies)
        })

        # Now write the updated list to json file
        with open('books/books.json','w') as booksFile:
            json.dump(bookList,booksFile,indent=4)
            return "Book Added Sucessfully"
    
    # Update Books
    def update_book(self,bookList:list,bookID:str,title,author,category,totalQTY:int,ageLimit:int,releaseDate):

        bookIndex = self.findBook(givenList=bookList,ID=bookID)

        if bookIndex is not None:
            issuedQTY = bookList[bookIndex]["issuedQTY"]


            totalQTY = int(totalQTY)
            if totalQTY:

                if totalQTY < issuedQTY:
                    return "Can't update because new Qty is less the books issued"

            try:

                updated_title = title if title else bookList[bookIndex]["title"]
                updated_author = author if author else bookList[bookIndex]["author"]
                updated_category = category if category is not [""] else bookList[bookIndex]["Category"]
                updated_totalQTY = totalQTY if totalQTY else bookList[bookIndex]["totalQTY"]
                updated_ageLimit = ageLimit if ageLimit else bookList[bookIndex]["ageLimit"]
                updated_releaseDate = releaseDate if releaseDate else bookList[bookIndex]["releaseDate"]
                copies  = updated_totalQTY - issuedQTY
                
            except:
                return "An Unexpected Error Occur"


            bookList[bookIndex] = {
                "BookID": bookID,
                "title": updated_title,
                "author": updated_author,
                "Category": updated_category,
                "ageLimit": updated_ageLimit,
                "releaseDate": updated_releaseDate,
                "copies": copies,
                "addedDate": datetime.now().strftime("%B %d, %Y"),
                "issuedQTY": issuedQTY,
                "totalQTY": updated_totalQTY
            }
            
            # Now write the updated list to json file
            with open('books/books.json','w') as booksFile:
                json.dump(bookList,booksFile,indent=4)
                return 'Book Updated Sucessfully'
        else:
            return "Can find Book with given (Book ID)"
        

    def delete_book(self,bookList:list,bookID:str):
        bookIndex = self.findBook(givenList=bookList,ID=bookID)

        if bookIndex is not None:
            issuedQTY = bookList[bookIndex]["issuedQTY"]
            if issuedQTY > 0 :
                return "Can't Delete Book, some book are issued"
            
            try:
                del bookList[bookIndex]
                with open('books/books.json','w') as booksFile:
                    json.dump(bookList,booksFile,indent=4)
                
                return "Book Deleted Sucessfully"
            except:
                return "Error while deleting Book try again!"
            

    def dynamic_search_by_title_or_ID(self,bookList:list, query):
        filtered_book_list = [book for book in bookList if(query in book["title"].lower()  or query in book["BookID"].lower())]
        return filtered_book_list
    
    def filter_by_category(self,bookList:list,category):
        filtered_books = [
            book for book in bookList
            if (category == '' or any(cat.lower() == category for cat in book['Category']))
        ]
        return filtered_books
    
    def filter_by_author(self,bookList:list,author):
        filtered_books = [
            book for book in bookList
            if (author == '' or author.lower() == book['author'].lower())
        ]
        return filtered_books