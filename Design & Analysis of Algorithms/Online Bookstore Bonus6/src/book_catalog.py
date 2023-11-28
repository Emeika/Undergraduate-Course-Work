from src.inventory_management import Inventory
class Book:
    def __init__(self, title, author, genre, price, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.availability = availability


class BookCatalog:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        self.books[book.title] = book
        inventory = Inventory()
        inventory.update_inventory(book, 1)
        

    def remove_book(self, title):
        if title in self.books:
            removed_book = self.books[title]
            del self.books[title]
            inventory = Inventory()
            inventory.update_inventory(removed_book, -1)
        
    def get_book_details(self, title):
        return self.books.get(title, None)

    def display_books(self):
        if not self.books:
            print("No books in the catalog.")
        else:
            print("\nBook Catalog:")
            for book in self.books.values():
                print(f"{book.title} by {book.author} - Genre: {book.genre}, Price: ${book.price}, Availability: {book.availability}")