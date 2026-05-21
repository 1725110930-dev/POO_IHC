class LibraryBook:
    def __init__(self, title, author, publisher, publication_year, genre, num_pages, language, isbn_code, shelf, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_year = publication_year
        self.genre = genre
        self.num_pages = num_pages
        self.language = language
        self.isbn_code = isbn_code
        self.shelf = shelf
        self.price = price
        self.borrowed = False
        self.times_borrowed = 0

    def displayData(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn_code)
        print("Location (Shelf):", self.shelf)

    def borrowBook(self):
        if not self.borrowed:
            self.borrowed = True
            self.times_borrowed += 1
            return f"The book '{self.title}' has been successfully borrowed."
        return f"Sorry, '{self.title}' is already borrowed."

    def returnBook(self):
        self.borrowed = False
        return f"The book '{self.title}' has been returned to the library."

    def changeShelf(self, new_shelf):
        self.shelf = new_shelf
        return f"The book was moved to shelf: {self.shelf}"

    def applyDiscount(self, percentage):
        self.price -= self.price * (percentage / 100)
        return f"New book price due to clearance: ${self.price:.2f}"


book1 = LibraryBook("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "Sudamericana Publishing", 1967, "Novel", 496, "Spanish", "978-0307474728", "Section A-3", 350.00)

book1.displayData()
print("-" * 30)
print(book1.borrowBook())
print(book1.returnBook())
print(book1.changeShelf("Section B-1"))
print(book1.applyDiscount(10))
