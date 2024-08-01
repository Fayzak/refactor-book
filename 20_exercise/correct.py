from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def fetch_order(self, order_id):
        pass

class NotificationInterface(ABC):
    @abstractmethod
    def send_notification(self, order):
        pass

class OrderProcessor:
    def __init__(self, db_interface, notification_interface):
        self.db_interface = db_interface
        self.notification_interface = notification_interface

    def process_order(self, order_id):
        order = self.db_interface.fetch_order(order_id)
        total = self.calculate_total(order)
        self.notification_interface.send_notification(order)
        return total

    def calculate_total(self, order):
        return sum(item["price"] for item in order["items"])

# Реальные реализации интерфейсов
class RealDatabase(DatabaseInterface):
    def fetch_order(self, order_id):
        print(f"Fetching real order {order_id} from database")
        return {"id": order_id, "items": [{"name": "Product1", "price": 100}, {"name": "Product2", "price": 150}]}

class RealNotification(NotificationInterface):
    def send_notification(self, order):
        print(f"Sending real notification for order {order['id']}")

# Тестовые реализации интерфейсов
class MockDatabase(DatabaseInterface):
    def fetch_order(self, order_id):
        print(f"Fetching mock order {order_id}")
        return {"id": order_id, "items": [{"name": "TestProduct", "price": 50}]}

class MockNotification(NotificationInterface):
    def send_notification(self, order):
        print(f"Sending mock notification for order {order['id']}")

# Пример использования в тестах
test_processor = OrderProcessor(MockDatabase(), MockNotification())
total = test_processor.process_order(123)
print(f"Test order total: {total}")
