class Inventory:
    def __init__(self):
        self.inventory = {}

    def update_inventory(self, book, quantity):
        if book.title in self.inventory:
            self.inventory[book.title] += quantity
        else:
            self.inventory[book.title] = quantity

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for title, quantity in self.inventory.items():
            print(f"{title}: {quantity} in stock")