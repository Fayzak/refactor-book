class Order:
    def __init__(self, order_id, items, total_amount):
        self.order_id = order_id
        self.items = items
        self.total_amount = total_amount

def process_order_data(order_id, total_amount):
    print(f"Processing order {order_id} with total {total_amount}")
    # Дополнительная логика обработки заказа

class OrderProcessor:
    def process_order(self, order):
        order_id = order.order_id
        total_amount = order.total_amount
        process_order_data(order_id, total_amount)

# Пример использования
order = Order(order_id="1234", items=["item1", "item2"], total_amount=99.99)
order_processor = OrderProcessor()
order_processor.process_order(order)  # Вывод: "Processing order 1234 with total 99.99"
