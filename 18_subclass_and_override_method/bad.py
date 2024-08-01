class ReportGenerator:
    def generate_report(self):
        data = self.get_data()
        self.save_to_file(data)

    def get_data(self):
        # Представим, что здесь сложная логика получения данных
        return "This is the report data"

    def save_to_file(self, data):
        with open("report.txt", "w") as file:
            file.write(data)
        print("Report saved to file")
