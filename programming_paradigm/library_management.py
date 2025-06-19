import sys

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True

        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' wasn't checked out.")

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
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print("Book not found.")
