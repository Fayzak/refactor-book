class DatabaseConnection:
    def connect(self):
        print("Connecting to the real database")

class ReportGenerator:
    def __init__(self):
        self.db_connection = self.create_db_connection()  # Фабричный метод

    def create_db_connection(self):
        return DatabaseConnection()  # Создание объекта

    def generate_report(self):
        self.db_connection.connect()
        print("Generating report using real database connection")

class MockDatabaseConnection:
    def connect(self):
        print("Connecting to a mock database")

class TestReportGenerator(ReportGenerator):
    def create_db_connection(self):
        return MockDatabaseConnection()  # Переопределение фабричного метода

# Пример использования
report_generator = ReportGenerator()
report_generator.generate_report()

# Пример использования тестирующего подкласса
test_report_generator = TestReportGenerator()
test_report_generator.generate_report()
