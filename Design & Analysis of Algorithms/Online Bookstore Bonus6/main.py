from src.book_catalog import Book, BookCatalog
from src.user_accounts import User, UserAccounts
from src.shopping_cart import ShoppingCart
from src.order_history import Order, OrderHistory
from src.inventory_management import Inventory
from src.search_and_filter import BookSearch
from src.recommendation_system import RecommendationSystem
from datetime import datetime

def main():
    # Creating instances of the modules
    book_catalog = BookCatalog()
    user_accounts = UserAccounts()
    shopping_cart = ShoppingCart()
    inventory = Inventory()
    order_history = OrderHistory()
    book_search = BookSearch(book_catalog)
    recommendation_system = RecommendationSystem(user_accounts, book_catalog, order_history)

    # Adding sample books to the catalog
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.99, 200)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 12.99, 150)
    book3 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", 15.99, 50)
    book4 = Book("Dark", "Unknown", "Fiction", 12.99, 8)
    book5 = Book("1984", "George Orwell", "Dystopian", 14.99, 15)

    book_catalog.add_book(book1)
    book_catalog.add_book(book2)
    book_catalog.add_book(book3)
    book_catalog.add_book(book4)
    book_catalog.add_book(book5)

    # Adding sample users
    user1 = User("Hafsah", "password123", "john@example.com")
    user2 = User("jane_smith", "qwerty456", "jane@example.com")
    user_accounts.add_user(user1)
    user_accounts.add_user(user2)

    while True:
        print("\nOptions:")
        print("1. Browse Books")
        print("2. Add a book to the shopping cart")
        print("3. Remove a book from the shopping cart")
        print("4. View shopping cart")
        print("5. Purchase items in the shopping cart")
        print("6. Search for books")
        print("7. View inventory")
        print("8. View order history")
        #print("9. Get recommendations")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        if choice == "1":
            # Browse Books
            book_catalog.display_books()

        elif choice == "2":
            # Add a book to the shopping cart
            title = input("Enter the title of the book to add to the shopping cart: ")
            book = book_catalog.get_book_details(title)
            if book:
                shopping_cart.add_to_cart(book)
                print(f"{book.title} added to the shopping cart.")
            else:
                print(f"Book with title '{title}' not found.")

        elif choice == "3":
            # Remove a book from the shopping cart
            title = input("Enter the title of the book to remove from the shopping cart: ")
            book = book_catalog.get_book_details(title)
            if book:
                shopping_cart.remove_from_cart(book.title)
                print(f"{book.title} removed from the shopping cart.")
            else:
                print(f"Book with title '{title}' not found.")

        elif choice == "4":
            # View shopping cart
            shopping_cart.display_cart()

        elif choice == "5":
            # Purchase items in the shopping cart
            if not shopping_cart.head:
                print("Shopping cart is empty. Add items before purchasing.")
                continue

            total_price = sum(book.price for book in shopping_cart.iterate_shopping_cart())
            order = Order(user1, total_price, [book.title for book in shopping_cart.iterate_shopping_cart()])
            for book in shopping_cart.iterate_shopping_cart():
                book_catalog.remove_book(book.title)
    
            order_history.save_to_file(order)
            shopping_cart.clear_cart()  # Clear the shopping cart after purchase
            print("Total Price", total_price)
            print("Purchase successful!")

        elif choice == "6":
            # Search for books
            print("\nSearch and Filter:")
            print("1. Search by Author")
            print("2. Search by Genre")
            print("3. Search by Title")
            
            search_choice = input("Enter your search choice (1-3): ")

            if search_choice == "1":
                author = input("Enter author name: ")
                books_by_author = BookSearch(book_catalog).search_by_author(author)
                print("\nBooks by", author + ":")
                for book in books_by_author:
                    print(f"{book.title} by {book.author}")

            elif search_choice == "2":
                genre = input("Enter genre: ")
                books_by_genre = BookSearch(book_catalog).search_by_genre(genre)
                print("\nBooks in", genre + " genre:")
                for book in books_by_genre:
                    print(f"{book.title} by {book.author}")

            elif search_choice == "3":
                title = input("Enter book title: ")
                book_details = book_catalog.get_book_details(title)
                if book_details:
                    print("\nBook Details:")
                    print(f"Title: {book_details.title}")
                    print(f"Author: {book_details.author}")
                    print(f"Genre: {book_details.genre}")
                    print(f"Price: ${book_details.price}")
                    print(f"Availability: {book_details.availability} copies")
                else:
                    print(f"Book with title '{title}' not found.")

        elif choice == "7":
            # View inventory
            book_catalog.display_inventory()

        elif choice == "8":
            # View order history
            order_history.display_order_history()

        elif choice == "9":
            # Get recommendations
            recommendations = recommendation_system.recommend_books(user1.username)
            print("\nRecommendations:")
            for book_title in recommendations:
                print(book_title)

        elif choice == "0":
            # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 9.")

if __name__ == "__main__":
    main()
