class GlobalContext:
    def __init__(self):
        self.database_connection = "Database Connection"
        self.config = {"debug": True, "version": "1.0"}

# Глобальный экземпляр нового класса
global_context = GlobalContext()

def fetch_data():
    if global_context.config["debug"]:
        print("Fetching data in debug mode")
    print(f"Using {global_context.database_connection} to fetch data")

# Пример использования
fetch_data()


# Для тестов
class MockGlobalContext:
    def __init__(self):
        self.database_connection = "Mock Database Connection"
        self.config = {"debug": False, "version": "test"}

# Замена глобального контекста на фиктивный для теста
global_context = MockGlobalContext()

fetch_data()  # Output: Using Mock Database Connection to fetch data
