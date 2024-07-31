class DatabaseConnection:
    def connect(self):
        print("Connecting to the real database")

class ReportGenerator:
    def __init__(self):
        self.db_connection = DatabaseConnection()  # Создание объекта внутри конструктора

    def generate_report(self):
        self.db_connection.connect()
        print("Generating report using real database connection")

# Пример использования
report_generator = ReportGenerator()
report_generator.generate_report()
