# Task: Library Management System (Session 5 task)

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = str(isbn)
        self.available = available

    def get_isbn(self):
        return self.__isbn
    
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Checked out"
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.__isbn}\nStatus: {status}\n")

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books = []
    
    def get_membership_id(self):
        return self.__membership_id
    
    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book is None:
            print("Book not found\n")
            return False
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.\n")
            return True
        else:
            print(f"Sorry, {book.title} is not available.\n")
            return False

    def return_book(self, book):
            if book in self.borrowed_books:
                book.available = True
                self.borrowed_books.remove(book)
                print(f"{self.name} returned {book.title}.\n")
                return True
            else:
                print(f"{self.name} cannot return {book.title} because it was not borrowed by them.\n")
                return False



class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Staff {self.name} added {book.title} to the library\n")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"Books in {self.name}: ")
        if not self.books:
            print("No books available\n")
        for book in self.books:
            book.display_info()



library = Library("Central Library")

staff = StaffMember("Mohamed", "M001", "S001")
member1 = Member("Mohy", "M002")

book1 = Book("Python Programming", "Guido van Rossum", "ISBN001")
book2 = Book("Data Science Basics", "Jane Doe", "ISBN002")
staff.add_book(library, book1)
staff.add_book(library, book2)

library.list_books()

member1.borrow_book(book1)
library.list_books()
member1.return_book(book1)
library.list_books()
