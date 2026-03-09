class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        print(self.title, self.author, self.pages)


b = Book("Harry Potter", "J.K. Rowling", 500)
b.book_info()

# N2

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(b.title, b.author)


b1 = Book("Harry Potter", "Rowling")
b2 = Book("1984", "Orwell")

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.show_books()