from src.inventory_management import Inventory

class Book:
    def __init__(self, title, author, genre, price, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.availability = availability  # composition

class BookCatalog:
    def __init__(self):
        self.books = {}
        self.inventory = Inventory()

    def add_book(self, book):
        self.books[book.title] = book
        self.inventory.update_inventory(book, book.availability)

    def delete_book(self, title):
        if title in self.books:
            removed_book = self.books[title]
            del self.books[title]
            self.inventory.update_inventory(removed_book, -removed_book.availability) # inventory class

    def remove_book(self, title): # purchase made single copy sold
        if title in self.books:
            removed_book = self.books[title]
            self.inventory.update_inventory(removed_book, -1)

    def get_book_details(self, title):
        return self.books.get(title, None)

    def display_books(self):
        if not self.books:
            print("No books in the catalog.")
        else:
            print("\nBook Catalog:")
            for book in self.books.values():
                print(f"{book.title} by {book.author} - Genre: {book.genre}, Price: ${book.price}, Availability: {book.availability}")

    def display_inventory(self):
        self.inventory.display_inventory()
