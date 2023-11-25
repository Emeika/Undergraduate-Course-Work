from src.book_catalog import Book, BookCatalog
from src.user_accounts import User, UserAccounts
from src.shopping_cart import ShoppingCart
from src.order_history import Order, OrderHistory
from src.inventory_management import Inventory
from src.search_and_filter import BookSearch
from src.recommendation_system import RecommendationSystem

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for title, quantity in inventory.inventory.items():
        print(f"{title}: {quantity} in stock")

def display_order_history(order_history):
    print("\nOrder History:")
    for order in order_history.orders:
        print(f"Order Date: {order.order_date} | User: {order.user.username} | Total Price: {order.total_price} | Items: {', '.join(order.purchased_items)}")

def main():
    # Creating instances of the modules
    book_catalog = BookCatalog()
    user_accounts = UserAccounts()
    shopping_cart = ShoppingCart()
    order_history = OrderHistory()
    inventory = Inventory()
    book_search = BookSearch(book_catalog)
    recommendation_system = RecommendationSystem(user_accounts, book_catalog, order_history)

    # Adding sample books to the catalog
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.99, 20)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 12.99, 15)
    book_catalog.add_book(book1)
    book_catalog.add_book(book2)

    # Adding sample users
    user1 = User("john_doe", "password123", "john@example.com")
    user2 = User("jane_smith", "qwerty456", "jane@example.com")
    user_accounts.add_user(user1)
    user_accounts.add_user(user2)

    while True:
        print("\nOptions:")
        print("1. Add a book to the shopping cart")
        print("2. Remove a book from the shopping cart")
        print("3. View shopping cart")
        print("4. Purchase items in the shopping cart")
        print("5. Search for books")
        print("6. View inventory")
        print("7. View order history")
        print("8. Get recommendations")
        print("0. Exit")

        choice = input("Enter your choice (0-8): ")

        if choice == "1":
            title = input("Enter the title of the book to add to the shopping cart: ")
            book = book_catalog.get_book_details(title)
            if book:
                shopping_cart.add_to_cart(book)
                print(f"{book.title} added to the shopping cart.")
            else:
                print(f"Book with title '{title}' not found.")
        elif choice == "2":
            title = input("Enter the title of the book to remove from the shopping cart: ")
            book = book_catalog.get_book_details(title)
            if book:
                shopping_cart.remove_from_cart(book)
                print(f"{book.title} removed from the shopping cart.")
            else:
                print(f"Book with title '{title}' not found.")
        elif choice == "3":
            print("\nShopping Cart:")
            for item in shopping_cart.items:
                print(f"{item.title} by {item.author}")
        elif choice == "4":
            # Simulating a purchase
            if not shopping_cart.items:
                print("Shopping cart is empty. Add items before purchasing.")
                continue

            total_price = sum(book.price for book in shopping_cart.items)
            order = Order(user1, total_price, [book.title for book in shopping_cart.items])
            order_history.add_order(order)
            inventory.update_inventory(book1, -1)
            inventory.update_inventory(book2, -1)
            shopping_cart.items = []  # Clear the shopping cart after purchase
            print("Purchase successful!")
        elif choice == "5":
            search_term = input("Enter search term (title, author, or genre): ")
            results = book_search.search_by_title(search_term) or \
                    book_search.search_by_author(search_term) or \
                    book_search.search_by_genre(search_term)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"{book.title} by {book.author}")
            else:
                print("No results found.")
        elif choice == "6":
            display_inventory(inventory)
        elif choice == "7":
            display_order_history(order_history)
        elif choice == "8":
            recommendations = recommendation_system.recommend_books(user1.username)
            print("\nRecommendations:")
            for book_title in recommendations:
                print(book_title)
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()
