import json
from datetime import date
from members.algorithms import Members
from books.algorithms import Books


class IssueBooks(Members,Books):
    def __init__(self):
        pass

    def generate_issue_book_id(self,issue_book_list):
        try:
          maxID = int(issue_book_list[-1]['IssueBookID'][1:])
          return f"I{maxID+1:03d}"
        except:
            return f"I{1:03d}"
        
    def search_issueBook(self,issue_book_list,issue_book_ID):
        left, right = 0, len(issue_book_list)-1
        while left <= right:
            middleIndex = (right+ left)//2
            midValue = int(issue_book_list[middleIndex]['IssueBookID'][1:])
            if midValue == int(issue_book_ID[1:]):
                return middleIndex
            elif midValue < int(issue_book_ID[1:]):
                left = middleIndex + 1
            else:
                right = middleIndex -1
        return None
            
    
    def issue_a_book(self,issue_book_list:list,memberID:str, bookID:str, expectedReturn):

        auto_generate_id = self.generate_issue_book_id(issue_book_list=issue_book_list)
        try:
            # getting the index of member through member ID
            try:
                with open('members/members.json', 'r') as membersFile:
                    members = json.load(membersFile)
                memberIndex = self.searhMember(membersList=members, ID=memberID)
                print(memberIndex)
                if memberIndex is None:
                    return "No member exists with such Member ID"
  
            except:
                return "Error While accessing Members database for member index"
            
            # getting the index of book through book ID
            try:
                with open('books/books.json', 'r') as booksFile:
                    books = json.load(booksFile)
                bookIndex = self.findBook(givenList=books, ID=bookID)
                if bookIndex is None:
                    return "No Book exists with such Book ID"
            except:
                return "Error While accessing Books database for book index"
            
            # Updating the Borrowed Books list with the new book ID
            try:
                
                books_borrowed = members[memberIndex]["Books Borrowed"]
                member_age = int(members[memberIndex]["age"])
                book_age_limit = int(books[bookIndex]["ageLimit"])

                # If member's borrowed_book list is empty then.........
                if not books_borrowed :
                    # compairing Member age with Book Age limit
                    if member_age < book_age_limit:
                        return "Can't issue Book Member's age is less than the book's age limit."

                    members[memberIndex].update({
                        "Books Borrowed": [bookID]
                    })

                    with open('members/members.json','w') as file:
                        json.dump(members,file, indent=4)

                elif books_borrowed and  len(books_borrowed) < 3: 

                    # Checking if same book exists in borrowed_book list
                    if any(bookID.lower() == borrowed.lower() for borrowed in books_borrowed):
                        return "Can't issue Book because Member already Borrowed same Book!"
                    else:  
                        # compairing Member age with Book Age limit
                        if member_age < book_age_limit:
                            return "Can't issue Book Member's age is less than the book's age limit."
   
                        books_borrowed.append(bookID)                
                        members[memberIndex].update({
                            "Books Borrowed": books_borrowed,
                        })

                        with open('members/members.json','w') as file:
                            json.dump(members,file, indent=4)
                else:
                    return "Can't Issue book because Member have already borrowed 3 Books!"
            except:
                return "Error While Updating Borrowed Books List of This Member"
            
            # updating avaible quantity of an issued Book
            try:
                available_copies = int(books[bookIndex]["copies"])
                issued_copies = int(books[bookIndex]["issuedQTY"])
                if available_copies > 0:
                    books[bookIndex].update({
                        "copies": available_copies - 1,
                        "issuedQTY": issued_copies +1
                    })
                    with open('books/books.json','w') as file:
                        json.dump(books,file, indent=4)
                else:
                    "Can't Issue Book because Not Enough Books Available!"
            except:
                return "Error While Updating  Book-Available Copies for this Book"


            issue_book_list.append({
                "IssueBookID": auto_generate_id,
                "memberID": memberID,
                "bookID": bookID,
                "expectedReturn":  str(expectedReturn) if expectedReturn else "Not-Confirmed",
                "issued_on": str(date.today()),
                "status": "issued",
                "return_date": None
            })
            with open('issuebooks/issueBooks.json','w') as file:
                json.dump(issue_book_list,file,indent=4)
            return "Book Issued Sucessfully"
        except Exception:
            return "Error while issuing Book Try Again!"

    def return_book(self,issue_book_list:list,issue_book_ID:str,memberID:str, bookID:str):
        issued_book_index = self.search_issueBook(issue_book_list=issue_book_list,issue_book_ID=issue_book_ID)
        if issue_book_list[issued_book_index]["status"] == "Received":
            return "This Issue invoice is already returned"
        print(issued_book_index)
        if issued_book_index is not None:
            # getting the index of member through member ID
            try:
                with open('members/members.json', 'r') as membersFile:
                    members = json.load(membersFile)
                memberIndex = self.searhMember(membersList=members, ID=memberID)
  
            except:
                return "Error While accessing Members database for member index"
            
            # getting the index of book through book ID
            try:
                with open('books/books.json', 'r') as booksFile:
                    books = json.load(booksFile)
                bookIndex = self.findBook(givenList=books, ID=bookID)
            except:
                return "Error While accessing Books database for book index"

            # Remove book from member's borrowed_book list
            try:
                books_borrowed = members[memberIndex]["Books Borrowed"]
                books_borrowed.remove(bookID)
                members[memberIndex].update({
                        "Books Borrowed": books_borrowed
                })
                with open('members/members.json','w') as file:
                    json.dump(members,file, indent=4)
            except:
                print("Error while removing book ID from Borrowed Book list")
                return "Error While Returning Book from Member"
            
            # Updating Copies available and issued copies in book.json
            try:
                available_copies = int(books[bookIndex]["copies"])
                issued_copies = int(books[bookIndex]["issuedQTY"])

                books[bookIndex].update({
                    "copies": available_copies + 1,
                    "issuedQTY": issued_copies -1,
                })
                with open('books/books.json','w') as file:
                    json.dump(books,file, indent=4)
            except:
                print("Error while updating available books count")
                return "Error While Returning Book from Member"
            
            # Updating status and return date in issuebooks database
            try:
                issue_book_list[issued_book_index].update({
                    "status": "Received",
                    "return_date": str(date.today())
                })
                with open('issuebooks/issueBooks.json', 'w') as file:
                    json.dump(issue_book_list,file,indent=4)
                return f"Book: {bookID} returned Sucessfully."
            except:
                print("Error while updating available status and return date in Issue Books database")
                return "Error While Returning Book from Member"
        else:
            return "Error While Returning Book from Member (Issue ID not found)"