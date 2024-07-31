class Order:
    def __init__(self, items, customer_type):
        self.items = items
        self.customer_type = customer_type

    def calculate_discount(self):
        if self.customer_type == "VIP":
            return 0.2
        elif sum(item['price'] * item['quantity'] for item in self.items) > 100:
            return 0.1
        else:
            return 0.0

# Пример использования
order = Order([{'price': 50, 'quantity': 2}, {'price': 30, 'quantity': 1}], "Regular")
print(order.calculate_discount())  # Output: 0.1
