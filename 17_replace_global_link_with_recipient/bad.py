config = {
    "db_host": "localhost",
    "db_port": 5432,
    "db_user": "user",
    "db_password": "password"
}

class DatabaseConnection:
    def connect(self):
        print(f"Connecting to {config['db_host']} on port {config['db_port']}")
        # Реальная логика подключения к базе данных
