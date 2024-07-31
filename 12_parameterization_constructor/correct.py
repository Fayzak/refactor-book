class PaymentService:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")

class OrderProcessor:
    def __init__(self, payment_service=None):
        if payment_service is None:
            payment_service = PaymentService()
        self.payment_service = payment_service

    def process_order(self, order_amount):
        print("Processing order")
        self.payment_service.process_payment(order_amount)

# Пример использования с параметризацией конструктора
order_processor = OrderProcessor()
order_processor.process_order(100)

# Пример использования с кастомным payment_service
class MockPaymentService(PaymentService):
    def process_payment(self, amount):
        print(f"[MOCK] Processing mock payment of {amount}")

mock_payment_service = MockPaymentService()
order_processor_with_mock = OrderProcessor(payment_service=mock_payment_service)
order_processor_with_mock.process_order(200)
