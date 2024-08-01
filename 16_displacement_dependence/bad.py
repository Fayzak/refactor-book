class PaymentGateway:
    def process_payment(self, amount):
        # Реальный код, связанный с обработкой платежа через внешний сервис
        print(f"Processing payment of ${amount} through PaymentGateway")
        return True

class PaymentProcessor:
    def __init__(self):
        self.gateway = PaymentGateway()

    def make_payment(self, amount):
        if amount > 0:
            return self.gateway.process_payment(amount)
        else:
            raise ValueError("Amount must be greater than zero")
