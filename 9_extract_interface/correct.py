from abc import ABC, abstractmethod

# Интерфейс
class PaymentProcessorInterface(ABC):
    @abstractmethod
    def process_credit_card(self, card_number, amount):
        pass

# Реализация интерфейса
class PaymentProcessor(PaymentProcessorInterface):
    def process_credit_card(self, card_number, amount):
        print(f"Processing credit card payment of {amount} for card number {card_number}")

# Пример использования
processor: PaymentProcessorInterface = PaymentProcessor()
processor.process_credit_card("1234-5678-9012-3456", 100.0)
