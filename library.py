# Name: Chirag Gupta
# Date:19-11-25
# Assignment: Library Inventory System - Library Logic

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # -------------------- BOOK FUNCTIONS --------------------
    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def get_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    # -------------------- MEMBER FUNCTIONS --------------------
    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    def get_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    # -------------------- BORROW & RETURN --------------------
    def lend_book(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.borrow_book(book):
                self.save_data()
                return True
        return False

    def take_return(self, member_id, isbn):
        member = self.get_member(member_id)
        book = self.get_book(isbn)

        if member and book:
            if member.return_book(book):
                self.save_data()
                return True
        return False

    # -------------------- FILE STORAGE --------------------
    def save_data(self):
        data = {
            "books": [
                {
                    "title": b.title,
                    "author": b.author,
                    "isbn": b.isbn,
                    "available": b.available,
                    "times_borrowed": b.times_borrowed
                } for b in self.books
            ],
            "members": [
                {
                    "name": m.name,
                    "member_id": m.member_id,
                    "borrowed_books": m.borrowed_books
                } for m in self.members
            ]
        }
        with open("library_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("library_data.json", "r") as f:
                data = json.load(f)

                for b in data["books"]:
                    book = Book(b["title"], b["author"], b["isbn"], b["available"])
                    book.times_borrowed = b["times_borrowed"]
                    self.books.append(book)

                for m in data["members"]:
                    member = Member(m["name"], m["member_id"])
                    member.borrowed_books = m["borrowed_books"]
                    self.members.append(member)
        except:
            pass

    # -------------------- ANALYTICS --------------------
    def report(self):
        total_borrowed = sum(1 for b in self.books if not b.available)
        most_borrowed = max(self.books, key=lambda b: b.times_borrowed, default=None)

        print("\n----- Library Report -----")
        print(f"Total Members: {len(self.members)}")
        print(f"Books Currently Borrowed: {total_borrowed}")

        if most_borrowed:
            print(f"Most Borrowed Book: {most_borrowed.title} ({most_borrowed.times_borrowed} times)")
        print("--------------------------\n")
