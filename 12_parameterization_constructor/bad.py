class PaymentService:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")

class OrderProcessor:
    def __init__(self):
        self.payment_service = PaymentService()  # Создание объекта внутри конструктора

    def process_order(self, order_amount):
        print("Processing order")
        self.payment_service.process_payment(order_amount)

# Пример использования
order_processor = OrderProcessor()
order_processor.process_order(100)
