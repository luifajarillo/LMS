from datetime import date

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def check_availability(self):
        return self.available_copies > 0

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False

class Member(Book):
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.books_borrowed.append(book)
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.return_book()
            return True
        else:
            return False

class Transaction:
    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.borrow_date = date.today()

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.\n")

    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.\n")

    def borrow_book(self, member_id, isbn):
        member = next((j for j in self.members if j.member_id == member_id),
None)
        book = next((sherraine for sherraine in self.books if sherraine.isbn
== isbn), None)
        if member and book:
            if member.borrow_book(book):
                self.transactions.append(Transaction(member, book))
                print("Book borrowed successfully.\n")
            else:
                print("Book not available for borrowing.\n")
        else:
            print("Member ID or ISBN not found.\n")

    def return_book(self, member_id, isbn):
        member = next((lee for lee in self.members if lee.member_id ==
member_id), None)
        book = next((s for s in self.books if s.isbn == isbn), None)
        if member and book:
            if member.return_book(book):
                print("Book returned successfully.\n")
            else:
                print("Book not borrowed by this member.\n")
        else:
            print("Member ID or ISBN not found.\n")

    def display_books(self):
        print("Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}\n")

    def display_members(self):
        print("Members:")
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}\n")

def main():
    library = Library()

    print("Welcome to Library Management System!\n")

    while True:
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            total_copies = int(input("Enter total copies: "))
            book = Book(title, author, isbn, total_copies)
            library.add_book(book)
        elif choice == '2':
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            member = Member(member_id, name)
            library.add_member(member)
        elif choice == '3':
            member_id = input("Enter member ID: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(member_id, isbn)
        elif choice == '4':
            member_id = input("Enter member ID: ")
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(member_id, isbn)
        elif choice == '5':
            library.display_books()
        elif choice == '6':
            library.display_members()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
