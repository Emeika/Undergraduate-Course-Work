# src/search_and_filter.py
class TreeNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, book):
        self.root = self._insert(self.root, book)

    def _insert(self, node, book):
        if node is None:
            return TreeNode(book)
        if book.title < node.book.title:
            node.left = self._insert(node.left, book)
        elif book.title > node.book.title:
            node.right = self._insert(node.right, book)
        return node

    def search_by_title(self, title):
        return self._search_by_title(self.root, title)

    def _search_by_title(self, node, title):
        if node is None or node.book.title == title:
            return node.book if node else None
        elif title < node.book.title:
            return self._search_by_title(node.left, title)
        else:
            return self._search_by_title(node.right, title)

class BookSearch:
    def __init__(self, book_catalog):
        self.book_catalog = book_catalog  # association
        self.title_tree = BinarySearchTree()
        for book in self.book_catalog.books.values():
            self.title_tree.insert(book)

    def search_by_author(self, author):
        return [book for book in self.book_catalog.books.values() if book.author == author]

    def search_by_genre(self, genre):
        return [book for book in self.book_catalog.books.values() if book.genre == genre]

    def search_by_title(self, title):
        return self.title_tree.search_by_title(title)
