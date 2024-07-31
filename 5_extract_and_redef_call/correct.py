class OrderProcessor:
    def process_order(self, order):
        self.validate_order(order)
        self.save_order(order)
        self.notify_order_processed(order)  # Используем новый метод

    def validate_order(self, order):
        print("Order validated")

    def save_order(self, order):
        print("Order saved")

    def send_notification(self, order):
        print("Notification sent")
    
    def notify_order_processed(self, order):  # Новый метод
        self.send_notification(order)

class TestOrderProcessor(OrderProcessor):
    def notify_order_processed(self, order):
        print("Test notification - no real notification sent")

# Пример использования
order_processor = TestOrderProcessor()
order_processor.process_order("Test Order")
