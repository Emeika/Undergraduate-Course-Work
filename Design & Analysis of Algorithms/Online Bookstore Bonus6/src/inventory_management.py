class Inventory:
    def __init__(self):
        self.inventory = {}

    def update_inventory(self, book, quantity):
        if book.title in self.inventory:
            self.inventory[book.title] += quantity
        else:
            self.inventory[book.title] = quantity
