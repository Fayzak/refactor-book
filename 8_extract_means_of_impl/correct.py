from abc import ABC, abstractmethod

# Интерфейс
class FileProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

# Реализация интерфейса
class FileProcessorImpl(FileProcessor):
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            # Обработка данных
            print(f"Processing data from {self.filename}")

# Пример использования
file_processor = FileProcessorImpl('example.txt')
file_processor.process()
