class Order:
    def __init__(self, items, discount):
        self.items = items
        self.discount = discount

    def calculate_total(self):
        calculator = OrderTotalCalculator(self)
        return calculator.calculate()

class OrderTotalCalculator:
    def __init__(self, order):
        self.order = order
        self.items = order.items
        self.discount = order.discount

    def calculate(self):
        total = sum(item['price'] * item['quantity'] for item in self.items)
        if self.discount:
            total -= total * self.discount
        return total

# Пример использования
order = Order([{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 3}], 0.1)
print(order.calculate_total())  # Output: 315.0
