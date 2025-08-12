

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from library.")
                return
        print(f"No book found with ISBN {isbn}.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                print(book.display_info())



library = Library()


book1 = Book("Clean Code", "Robert C. Martin", "9780132350884")
book2 = Book("The Pragmatic Programmer", "Andrew Hunt", "9780201616224")
book3 = Book("Python Crash Course", "Eric Matthes", "9781593276034")


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.list_books()


library.remove_book("9780201616224")


library.list_books()
