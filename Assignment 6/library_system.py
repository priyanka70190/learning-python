"""
build a mini library mgmt system using functions and global variables.
create the following global variables:
library --> a list of dictionaries,each containing title,author,copies
borrowed _books --> a dictionary storing
{book_title:borrower_name}
preload the library with 5 books with varying copies
create following functions:
show_all_books()-->loops through and displays all the books with availability
search_book(title)--->searches for a book and display its details,shows"Not Found" if absent
borrow_book(title,borrower)--> allow borrowing if copies are available,reduce copy count by 1,
records in borrowed books,rejects if no copy left
return_book(title,borrower)-->processes return only if that borrower has borrowed the book,increases copy
count by 1,removes from borrowed books
show_borrowed()-->displays all currently borrowed books with borrower names
Run a loop presenting a menu:
Show All/Search/Borrow/Return/Borrowed List/Exit."""

library=[{"Title":"The Great Gatsby","Author":"F.Scott Fitzgerald","Copies":3},
         {"Title":"To Kill a Mocking Bird","Author":"Harper Lee","Copies":2},
         {"Title":"1984","Author":"George Orwell","Copies":1},
         {"Title":"Harry Porter","Author":"J.K. Rowling","Copies":4},
         {"Title":"The Alchemist","Author":"Paulo Coelho","Copies":2}]
borrowed_books=[{"book_title":"1984","borrower_name":"john"},]
def show_all_books():
    i=1
    j=0
    for key in library:
        print(i,". ",library[j]["Title"],"   | ",library[j]["Author"],"   | ",library[j]["Copies"])
        j=j+1
        i=i+1

def borrow_book(title,borrower):
    j=0
    for key in library:
        if library[j]["Title"]==title:
            if library[j]["Copies"]>0:
                library[j]["Copies"]-=1
                print("Success! ",borrower," has borrowed ",library[j]["Title"],
                      ". Copies Remaining: ",library[j]["Copies"] )
            else:
                print("sorry..! no copies of ",library[j]["Title"],"are available")
        j=j+1

def show_borrowed():
    j=0
    i=1
    print("Currently borrowed books:")
    for key in borrowed_books:
       print(i,". ","\"",borrowed_books[j]["book_title"],"\" borrowed by ",borrowed_books[j]["borrower_name"])
       i=i+1


def return_book(title,borrower):
    j=0
    for key in borrowed_books:
        if borrowed_books[j]["book_title"]==title and borrowed_books[j]["borrower_name"]==borrower:
            k=0
            for key in library:

                if library[k]["Title"]==title:
                       library[k]["Copies"]+=1
                       break
                k=k+1
    print("\"",title,"\" returned successfully by john.Copies available",library[k]["Copies"])
    for key in borrowed_books:
        if key.get("book_title")==title and key.get("borrower_name")==borrower:
            borrowed_books.remove(key)

def search_book(title):
    j=0
    for key in library:
        if library[j]["Title"]==title:
            print("Book Details:")
            print(library[j]["Title"],"  | ",library[j]["Author"],"   | ",library[j]["Copies"])
            break

        else:
          j=j+1
          if(j==len(library)):
              print("sorry..! no books available")



print("--- Library Menu ---")
print("1. show all books")
print("2. search book")
print("3. borrow book")
print("4. return book")
print("5. show borrowed books")
print("6. exit")
print(25*"-")
while(True):
    print("Enter your choice:")
    choice=int(input())
    if(choice==1):
        show_all_books()
    elif(choice==2):
        print("Enter book Title: ")
        title=input()
        search_book(title)
    elif(choice==3):
        print("Enter Title of book u wanna borrow: ")
        title=input()
        print("Enter borrower name:")
        borrower=input()
        borrow_book(title,borrower)
    elif(choice==4):
        print("Enter book Title: ")
        title=input()
        print("Enter your name: ")
        borrower=input()
        return_book(title,borrower)
    elif(choice==5):
        show_borrowed()
    else:
        print("good bye")
        break


