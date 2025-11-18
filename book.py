# Name: Chirag Gupta
# Assignment: Library Inventory System - Book Class

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.times_borrowed = 0

    def borrow(self):
        if self.available:
            self.available = False
            self.times_borrowed += 1
            return True
        return False

    def return_book(self):
        self.available = True
