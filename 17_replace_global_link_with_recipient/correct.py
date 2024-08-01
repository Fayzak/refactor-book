config = {
    "db_host": "localhost",
    "db_port": 5432,
    "db_user": "user",
    "db_password": "password"
}

class DatabaseConnection:
    def get_config(self):
        return config

    def connect(self):
        config = self.get_config()
        print(f"Connecting to {config['db_host']} on port {config['db_port']}")
        # Реальная логика подключения к базе данных

class TestDatabaseConnection(DatabaseConnection):
    def get_config(self):
        return {
            "db_host": "test_host",
            "db_port": 9999,
            "db_user": "test_user",
            "db_password": "test_password"
        }

# Реальное подключение
real_db = DatabaseConnection()
real_db.connect()

# Тестовое подключение
test_db = TestDatabaseConnection()
test_db.connect()
