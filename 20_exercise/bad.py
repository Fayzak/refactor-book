class OrderProcessor:
    def __init__(self, db_host, db_user, db_password):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password

    def connect_to_db(self):
        # Прямое подключение к базе данных
        print(f"Connecting to database at {self.db_host} with user {self.db_user}")
        # Имитируем подключение к базе данных
        return "DatabaseConnectionObject"

    def fetch_order(self, order_id):
        db_conn = self.connect_to_db()
        print(f"Fetching order {order_id} from database using {db_conn}")
        # Возвращаем фиктивный заказ для примера
        return {"id": order_id, "items": [{"name": "Product1", "price": 100}, {"name": "Product2", "price": 150}]}

    def calculate_total(self, order):
        total = sum(item["price"] for item in order["items"])
        print(f"Total price for order {order['id']} is {total}")
        return total

    def send_notification(self, order):
        print(f"Sending notification for order {order['id']}")
        # Имитируем отправку уведомления

    def process_order(self, order_id):
        order = self.fetch_order(order_id)
        total = self.calculate_total(order)
        self.send_notification(order)
        return total
