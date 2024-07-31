class Order:
    def __init__(self, order_id, items, total_amount):
        self.order_id = order_id
        self.items = items
        self.total_amount = total_amount

class OrderProcessor:
    def process_order(self, order):
        print(f"Processing order {order.order_id} with total {order.total_amount}")
        # Дополнительная логика обработки заказа
