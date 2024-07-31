class FileProcessor:
    def __init__(self, filename):
        self.filename = filename

    def process(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            # Обработка данных
            print(f"Processing data from {self.filename}")
