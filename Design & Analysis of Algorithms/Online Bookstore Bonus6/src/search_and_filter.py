# src/search_and_filter.py
class BookSearch:
    def __init__(self, book_catalog):
        self.book_catalog = book_catalog

    def search_by_author(self, author):
        return [book for book in self.book_catalog.books.values() if book.author == author]

    def search_by_genre(self, genre):
        return [book for book in self.book_catalog.books.values() if book.genre == genre]

    def search_by_title(self, title):
        return self.book_catalog.get_book_details(title)
