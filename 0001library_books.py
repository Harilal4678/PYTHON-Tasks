class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

class library(Book):
    def __init__(self):
        self.books=[]
    def add_book(self,title,author,isbn):
        book=Book(title,author,isbn)
        self.books.append(book)

    def remove(self,isbn):
        for book in self.books:
            if isbn == book.isbn:
                self.books.remove(book)
                print(f"book with title {book.title} removed successfully of id {book.isbn}")


    

    def search(self,title):
        for book in self.books:
            if book.title == title:
                return(f"searched book available: {book.title} by {book.author}")
            else:
                return "not available"


library=library()
library.add_book("programming","hari","76")
library.add_book("django","asheen","77")
library.remove("77")
s=library.search("programming")

print(s)


