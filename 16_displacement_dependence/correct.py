from abc import ABC, abstractmethod

class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} through PaymentGateway")
        return True

class PaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class RealPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.gateway = PaymentGateway()

    def make_payment(self, amount):
        if amount > 0:
            return self.gateway.process_payment(amount)
        else:
            raise ValueError("Amount must be greater than zero")

class MockPaymentGateway:
    def process_payment(self, amount):
        print(f"Mock processing payment of ${amount}")
        return True

class TestPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.gateway = MockPaymentGateway()

    def make_payment(self, amount):
        if amount > 0:
            return self.gateway.process_payment(amount)
        else:
            raise ValueError("Amount must be greater than zero")

# Тесты
def test_make_payment():
    processor = TestPaymentProcessor()
    assert processor.make_payment(100) == True

def test_make_payment_invalid_amount():
    processor = TestPaymentProcessor()
    try:
        processor.make_payment(-10)
    except ValueError as e:
        assert str(e) == "Amount must be greater than zero"

# Запуск тестов
test_make_payment()
test_make_payment_invalid_amount()
print("Все тесты пройдены")
