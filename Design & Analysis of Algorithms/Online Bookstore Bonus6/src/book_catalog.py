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

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
        
    def get_book_details(self, title):
        return self.books.get(title, None) 