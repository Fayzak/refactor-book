class OrderProcessor:
    def process_order(self, order):
        self.validate_order(order)
        self.save_order(order)
        self.send_notification(order)

    def validate_order(self, order):
        # Логика валидации заказа
        print("Order validated")

    def save_order(self, order):
        # Логика сохранения заказа
        print("Order saved")

    def send_notification(self, order):
        # Логика отправки уведомления
        print("Notification sent")
