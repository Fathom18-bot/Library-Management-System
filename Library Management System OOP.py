# LIBRARY MANAGEMENT SYSTEM (short OOP version)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False


Books = [
    Book("Othello", "William Shakespeare"),
    Book("Harvest of Corruption", "Frank Ogodo Ogbeche"),
    Book("The Blood of a Stranger", "Dele Charley"),
    Book("She Stoops to Conquer", "Oliver Goldsmith"),
    Book("A Raisin in the Sun", "Lorraine Hansberry"),
]


def find_book(title):
    for book in Books:
        if book.title.lower() == title.lower():
            return book
    return None


class Libarian:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_book(self, title, author):
        Books.append(Book(title, author))
        print("Successfully added", title)

    def remove_book(self, title):
        book = find_book(title)
        if book:
            Books.remove(book)
            print("Successfully removed", title)
        else:
            print("Book not found")

    def menu(self):
        while True:
            option = input("\n1. Add a Book \n2. Remove a Book \n3. Logout \n: ")
            if option == "1":
                self.add_book(input("Enter Book title: "), input("Enter Book author: "))
            elif option == "2":
                self.remove_book(input("Title of the book you want to remove: "))
            elif option == "3":
                break
            else:
                print("Invalid input")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def view_books(self):
        for book in Books:
            status = "Borrowed" if book.borrowed else "Available"
            print(f"{book.title} by {book.author} [{status}]")

    def search_book(self, word):
        for book in Books:
            if word.lower() in book.title.lower() or word.lower() in book.author.lower():
                print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        book = find_book(title)
        if book is None:
            print("Book not found")
        elif book.borrowed:
            print("Sorry, already borrowed")
        else:
            book.borrowed = True
            print("You have borrowed", book.title)

    def return_book(self, title):
        book = find_book(title)
        if book and book.borrowed:
            book.borrowed = False
            print("You have returned", book.title)
        else:
            print("This book was not borrowed")

    def menu(self):
        while True:
            option = input("\n1. View all books \n2. Search \n3. Borrow \n4. Return \n5. Exit \n: ")
            if option == "1":
                self.view_books()
            elif option == "2":
                self.search_book(input("Enter title or author: "))
            elif option == "3":
                self.borrow_book(input("Title to borrow: "))
            elif option == "4":
                self.return_book(input("Title to return: "))
            elif option == "5":
                break
            else:
                print("Invalid input")


Accounts = {"admin": Libarian("admin", "1234")}


def start():
    while True:
        print("\nWELCOME to School 2 Library")
        choice = input("1. Signup \n2. Login \n3. Exit \n: ")

        if choice == "1":
            username = input("Username: ")
            role = input("Sign up as: \n1. Libarian \n2. User \n: ")
            password = input("Password: ")
            if username in Accounts:
                print("Username already taken")
            elif role == "1":
                Accounts[username] = Libarian(username, password)
                print("Signup successful")
            elif role == "2":
                Accounts[username] = User(username, password)
                print("Signup successful")
            else:
                print("Invalid input")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            account = Accounts.get(username)
            if account and account.password == password:
                print("Login Successful, welcome", username)
                account.menu()
            else:
                print("Wrong username or password")

        elif choice == "3":
            print("Thank you for visiting School 2 Library")
            break
        else:
            print("Invalid input")


start()