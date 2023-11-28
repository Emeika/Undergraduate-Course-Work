class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class ShoppingCart:
    def __init__(self):
        self.head = None

    def add_to_cart(self, book):
        new_node = Node(book)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_from_cart(self, title):
        if not self.head:
            return

        if self.head.book.title == title:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.book.title == title:
                current.next = current.next.next
                return
            current = current.next

    def iterate_shopping_cart(self):
        current = self.head
        while current:
            yield current.book
            current = current.next

    def display_cart(self):
        if not self.head:
            print("Cart is empty")
        current = self.head
        while current:
            print(f"{current.book.title} by {current.book.author}")
            current = current.next
        
    def clear_cart(self):
        self.head = None
