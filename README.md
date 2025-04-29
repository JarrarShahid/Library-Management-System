# Library-Management-System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-application%2Fjson-black?logo=json&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)


A full-stack, JSON-backed Library Management System built to demonstrate core Data Structures & Algorithms concepts, clean OOP design, and a modern Django web stack.

---

## 🚀 Table of Contents
1. [About the Project](#about-the-project)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
5. [File Structure](#file-structure)  
6. [Usage](#usage)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)

---

## 📖 About the Project
This Library Management System allows librarians to manage members, books, and issue/return workflows with:

- **Efficient storage** in JSON files (one per domain: members, books, issueRecords).  
- **Binary-search lookups** on IDs (O(log n) performance).  
- **Automatic ID generation** & duplicate detection.  
- **Business rules**: age-limit enforcement, 3-book borrow cap, and real-time copy counts.  
- **Modular OOP design** with three Python classes:
  - `Members` — add/update/delete/search members  
  - `Books` — add/update/delete/search books  
  - `IssueBooks` — issue & return logic, inherits from both  

A Django backend wires these algorithms into HTML/CSS/JS views for a seamless librarian dashboard experience.

---

## ✨ Features
- **Member Management**  
  - Add, update, and delete members  
  - Automatic `MXXX` ID generation  
  - Duplicate-check by name, age & contact  
- **Book Management**  
  - Add, update, and delete books  
  - Automatic `BXXX` ID generation  
  - Track total, available & issued copies  
- **Issue & Return Workflow**  
  - Auto-generated `IXXX` issue IDs  
  - Enforce age limits & max 3 books per member  
  - Real-time copy count updates  
  - Stamp issue date & return date  

---

## 🛠 Tech Stack
- **Backend**: Python 3 • Django  
- **Data Storage**: JSON files (`members/members.json`, `books/books.json`, `issuebooks/issueBooks.json`)  
- **Frontend**: HTML • CSS • JavaScript  
- **Version Control**: Git & GitHub  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+  
- pip (package manager)  
- Git  

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/JarrarShahid/Library-Management-System.git
   cd LibraryManagementSystem

2. **Create a virtual environment & install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # macOS/Linux
    venv\Scripts\activate       # Windows
    pip install -r requirements.txt

3. **Initialize JSON data files**
    Ensure the following files exist (empty list [] if fresh):

    members/members.json

    books/books.json

    issuebooks/issueBooks.json

4. **Run Django development server**
   ```bash
   python manage.py migrate
   python manage.py runserver

## 🗂 File Structure
```
LIBRARYMANAGEMENT/
│
├── authentication/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── users.json
│   └── views.py
│
├── books/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── books.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── issuebooks/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── issueBooks.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── libraryManagement/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── members/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── members.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── issueTemplates/
│   │   ├── issueBook.html
│   │   ├── issueBooksPreview.html
│   │   └── returnBook.html
│   │
│   ├── memberTemplates/
│   │   ├── addMember.html
│   │   ├── deleteMember.html
│   │   ├── membersPreview.html
│   │   └── updateMember.html
│   │
│   ├── addBooksPage.html
│   ├── base.html
│   ├── booksPreview.html
│   ├── deleteBook.html
│   ├── login.html
│   └── updateBook.html
│
├── db.sqlite3
└── manage.py
LIBRARYMANAGEMENT/
│
├── authentication/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── users.json
│   └── views.py
│
├── books/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── books.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── issuebooks/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── issueBooks.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── libraryManagement/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── members/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── algorithms.py
│   ├── apps.py
│   ├── members.json
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── issueTemplates/
│   │   ├── issueBook.html
│   │   ├── issueBooksPreview.html
│   │   └── returnBook.html
│   │
│   ├── memberTemplates/
│   │   ├── addMember.html
│   │   ├── deleteMember.html
│   │   ├── membersPreview.html
│   │   └── updateMember.html
│   │
│   ├── addBooksPage.html
│   ├── base.html
│   ├── booksPreview.html
│   ├── deleteBook.html
│   ├── login.html
│   └── updateBook.html
│
├── db.sqlite3
└── manage.py
```

## 🔧 Usage Examples
```
from members.algorithms import Members
from books.algorithms import Books
from issuebooks.algorithms import IssueBooks
import json

# Load current data
with open('members/members.json') as f: members = json.load(f)
with open('books/books.json')   as f: books   = json.load(f)
with open('issuebooks/issueBooks.json') as f: issues = json.load(f)

# Instantiate handlers
member_mgr = Members()
book_mgr   = Books()
issue_mgr  = IssueBooks()

# Add a new member
res = member_mgr.add_members(members, name="Alice", age=30, contact="555-1234", address="123 Maple St.")
print(res)  # "Member Added Successfully"

# Add a new book
res = book_mgr.add_a_book(books, title="1984", author="George Orwell",
                         category=["Dystopian"], copies=5, ageLimit=15, releaseDate="1949-06-08")
print(res)  # "Book Added Successfully"

# Issue a book
res = issue_mgr.issue_a_book(issues, memberID="M001", bookID="B001", expectedReturn="2025-05-15")
print(res)  # "Book Issued Successfully"
```

## 🤝 Contributing
We welcome contributions!

1. Fork the project
2. Create a feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -m 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Open a Pull Request

Please adhere to the existing code style and include tests where applicable.

## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

## Acknowledgements
[Maaz Rehan](https://github.com/Maaz-Bin-Haider)

[Fawad Ahmed](https://github.com/Fawad992005)

[Zahid Rasheed](https://github.com/Zahid275)

[Saym Bin Aziz](https://github.com/SaymbinAziz)
   
