class RecommendationSystem:
    def __init__(self, user_accounts, book_catalog, order_history):
        self.user_accounts = user_accounts
        self.book_catalog = book_catalog
        self.order_history = order_history

    def recommend_books(self, username, num_recommendations=3):
        """
        Recommend books to a user based on their purchase history.

        Parameters:
        - username (str): The username of the user for whom recommendations are needed.
        - num_recommendations (int): Number of books to recommend. Default is 3.

        Returns:
        - list: A list of recommended book titles.
        """
        user = self.user_accounts.get_user_details(username)

        if user is None:
            print(f"User with username '{username}' not found.")
            return []

        # Gather purchased items from the user's order history
        purchased_items = []
        for order in self.order_history.orders:
            if order.user.username == username:
                purchased_items.extend(order.purchased_items)

        # Count the occurrences of each book in the purchase history
        book_counts = {}
        for item in purchased_items:
            book_counts[item] = book_counts.get(item, 0) + 1

        # Sort books by purchase count in descending order
        sorted_books = sorted(book_counts.items(), key=lambda x: x[1], reverse=True)

        # Extract recommended book titles (excluding those already purchased)
        recommendations = [book[0] for book in sorted_books if book[0] not in purchased_items][:num_recommendations]

        return recommendations
