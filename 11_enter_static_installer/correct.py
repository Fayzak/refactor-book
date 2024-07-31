class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def connect(self):
        print("Connecting to the database")

    @staticmethod
    def set_instance(instance):
        DatabaseConnection._instance = instance

class MockDatabaseConnection(DatabaseConnection):
    def connect(self):
        print("Mock connection to the database")

# Пример использования
db = DatabaseConnection()
db.connect()  # Вывод: "Connecting to the database"

mock_db = MockDatabaseConnection()
DatabaseConnection.set_instance(mock_db)

db = DatabaseConnection()
db.connect()  # Вывод: "Mock connection to the database"
