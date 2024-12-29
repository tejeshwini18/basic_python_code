"""Create a class Book with attributes:
title (string)
author (string)
copies (integer)
Library Class:

The Library class should have:
A list of books to store all the books.
Methods:
add_book(book: Book) – Adds a book to the library.
borrow_book(title: str) – Reduces the available copies by 1 if the book is available. If not, print "Book not available."
return_book(title: str) – Increases the available copies by 1 when a book is returned.
display_books() – Displays all available books with their titles, authors, and the number of copies.
Main Logic:

Create a Library instance and perform some operations:
Add books to the library.
Borrow a few books.
Display the library status.
Return a book and display the status again"""

class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - Copies available: {self.copies}"

    def reduce_copies(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"One copy of '{self.title}' has been borrowed. Copies left: {self.copies}")
        else:
            print(f"No more copies of '{self.title}' available to borrow.")

    def add_copies(self):
        self.copies += 1
        print(f"One copy of '{self.title}' has been returned. Total copies: {self.copies}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.reduce_copies()
                return
        print(f"The book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.add_copies()
                return
        print(f"The book '{title}' is not available in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)


# Example usage:

# Creating a library instance
library = Library()

# Adding books with available copies to the library
book1 = Book('1984', 'George Orwell', 1949, 5)
book2 = Book('To Kill a Mockingbird', 'Harper Lee', 1960, 3)

library.add_book(book1)
library.add_book(book2)

# Display all books in the library
library.display_books()

# Borrowing a book
library.borrow_book('1984')

# Returning a book (increases by 1 copy)
library.return_book('1984')

# Display the updated list of books
library.display_books()
