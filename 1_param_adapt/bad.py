class Database:
    def fetch_data(self):
        # Представьте, что здесь сложная логика работы с базой данных
        return "Real Data"

class DataProcessor:
    def __init__(self, database):
        self.database = database

    def process(self):
        data = self.database.fetch_data()
        print(f"Processing: {data}")

# Пример использования
db = Database()
processor = DataProcessor(db)
processor.process()
