import sys

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def list_available_books(self):
        if len(self._books) > 0:
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")
        else:
            print("No books available.")

    def check_out_book(self, title):
        for product in self._books:
            if product.title == title:
                product._is_checked_out = True
                return
        print("book is not available")

    def return_book(self, title):
        for product in self._books:
            if product.title == title:
                product._is_checked_out = False
                return
        print("book is not available")

