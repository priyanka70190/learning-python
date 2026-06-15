"""
Define a class called Book with attributes title, author, and is_available (default True).
Define another class called Library with an attribute books,
 which is a list of Book objects. Add three methods to Library:
  - add_book(book): adds a book to the list
  - borrow_book(title): sets is_available to False if found and available,
   otherwise print a suitable message
  - show_books(): prints all books with their author and availability status

Create a Library object, add at least 3 books, borrow one, and display the full list.

"""

class Book:
    def __init__(self,title,author,is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

class Library:
    def __init__(self,books):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.is_available = False
                #self.books.remove(book)
            else:
                book.is_available = True
            return
        print(f"Book '{title}' not found.")


    def show_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Available: {book.is_available}")

library=Library("books")
library.add_book(Book("The Great Gatsby","F. Scott Fitzgerald"))
library.add_book(Book("To Kill a Mockingbird","Harper Lee"))
library.add_book(Book("Clean Code","Robert C. Martin"))
library.show_books()
#library.borrow_book(library.books[0])
library.borrow_book("The Great Gatsby")
library.show_books()

