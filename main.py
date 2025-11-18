# Name: Chirag Gupta
# Date:19-11-25
# Assignment: Library Inventory System - Main Menu

from library import Library

library = Library()

print("📚 Welcome to the Library Inventory System")

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Library Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        library.add_book(title, author, isbn)
        print("Book Added Successfully")

    elif choice == "2":
        name = input("Member Name: ")
        mid = input("Member ID: ")
        library.register_member(name, mid)
        print("Member Registered Successfully")

    elif choice == "3":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        if library.lend_book(mid, isbn):
            print("Book Borrowed Successfully")
        else:
            print("Borrow Failed")

    elif choice == "4":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        if library.take_return(mid, isbn):
            print("Book Returned Successfully")
        else:
            print("Return Failed")

    elif choice == "5":
        library.report()

    elif choice == "6":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice")
