# 1. Создаем новый интерфейс
class DataSource:
    def fetch_data(self):
        raise NotImplementedError

# 2. Реализуем интерфейс в выходном коде
class Database(DataSource):
    def fetch_data(self):
        return "Real Data"

# 3. Создаем фиктивное средство реализации интерфейса
class MockDataSource(DataSource):
    def fetch_data(self):
        return "Mock Data"

# 5. Вносим изменения в метод
class DataProcessor:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def process(self):
        data = self.data_source.fetch_data()
        print(f"Processing: {data}")

# 4. Составляем простой контрольный пример
if __name__ == "__main__":
    # Используем фиктивный объект для тестирования
    mock_data_source = MockDataSource()
    processor = DataProcessor(mock_data_source)

    # 6. Проверяем возможность тестирования
    processor.process()  # Output: Processing: Mock Data
