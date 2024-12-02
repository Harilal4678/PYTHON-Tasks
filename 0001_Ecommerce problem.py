class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class Order:
    def __init__(self, items, tax_rate=0.1, discount_rate=0.05):
        self.items = items
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate

    def calculate_total_price(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        tax = subtotal * self.tax_rate
        discount = subtotal * self.discount_rate
        return subtotal + tax - discount

user = User("Hari")

order1 = Order([
    {"name": "Laptop", "price": 1000, "quantity": 1},
    {"name": "Mouse", "price": 50, "quantity": 2}
])

order2 = Order([
    {"name": "Monitor", "price": 300, "quantity": 1},
    {"name": "Keyboard", "price": 100, "quantity": 1}
])

user.place_order(order1)
user.place_order(order2)

for i, order in enumerate(user.orders, 1):
    print(f"Order {i} Total: {order.calculate_total_price()}")
