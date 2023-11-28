from src.user_accounts import UserAccounts
from datetime import datetime

class Order:
    def __init__(self, user, total_price, purchased_items):
        self.order_date = datetime.now()
        self.user = user
        self.total_price = total_price
        self.purchased_items = purchased_items

class OrderHistory:
    def __init__(self):
        self.user_accounts = UserAccounts()

    def save_to_file(self, order):
        with open('Online Bookstore Bonus6\src\order_history.txt', 'a') as file:
            file.write(f"{order.order_date} | {order.user.username} | Total Price: {order.total_price} | Items: {', '.join(order.purchased_items)}\n")

    def display_order_history(self):
        try:
            with open('Online Bookstore Bonus6\src\order_history.txt', 'r') as file:
                print("Order History:")
                for line in file:
                    parts = line.strip().split('|')
                    order_date = datetime.strptime(parts[0].strip(), '%Y-%m-%d %H:%M:%S.%f')
                    username = parts[1].strip()
                    total_price = float(parts[2].split(':')[1].strip())
                    purchased_items = [item.strip() for item in parts[3].split(':')[1].strip().split(',')]
                    
                    # Retrieve the user object from user_accounts based on the username
                    current_user = self.user_accounts.get_user_details(username)
                    print(current_user)
                    if current_user is not None:
                        order = Order(current_user, total_price, purchased_items)
                        order.order_date = order_date  # Set the order date
                        print(f"Order Date: {order_date} | User: {order.user.username} | Total Price: {order.total_price} | Items: {', '.join(order.purchased_items)}")
                    else:
                        #print(f"User with username '{username}' not found.")
                        order = Order(current_user, total_price, purchased_items)
                        order.order_date = order_date  # Set the order date
                        print(f"Order Date: {order_date} | User: Hafsah | Total Price: {order.total_price} | Items: {', '.join(order.purchased_items)}")
        except FileNotFoundError:
            print("No order history found.")
