from datetime import datetime

class Order:
    def __init__(self, user, total_price, purchased_items):
        self.order_date = datetime.now()
        self.user = user
        self.total_price = total_price
        self.purchased_items = purchased_items

    def save_to_file(self):
        with open('order_history.txt', 'a') as file:
            file.write(f"{self.order_date} | {self.user.username} | Total Price: {self.total_price} | Items: {', '.join(self.purchased_items)}\n")

    @staticmethod
    def display_order_history():
        with open('order_history.txt', 'r') as file:
            print("Order History:")
            for line in file:
                parts = line.strip().split('|')
                order_date = datetime.strptime(parts[0].strip(), '%Y-%m-%d %H:%M:%S.%f')
                username = parts[1].strip()
                total_price = float(parts[2].split(':')[1].strip())
                purchased_items = [item.strip() for item in parts[3].split(':')[1].strip().split(',')]
                order = Order(username, total_price, purchased_items)
                print(f"Order Date: {order_date} | User: {order.user.username} | Total Price: {order.total_price} | Items: {', '.join(order.purchased_items)}")
