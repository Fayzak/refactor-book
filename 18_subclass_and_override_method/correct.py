class ReportGenerator:
    def generate_report(self):
        data = self.get_data()
        self.save_to_file(data)

    def get_data(self):
        return "This is the report data"

    def save_to_file(self, data):
        with open("report.txt", "w") as file:
            file.write(data)
        print("Report saved to file")

class TestReportGenerator(ReportGenerator):
    def save_to_file(self, data):
        self.test_output = data
        print("Report saved to test_output")

# Тест
def test_generate_report():
    test_generator = TestReportGenerator()
    test_generator.generate_report()
    assert test_generator.test_output == "This is the report data"

# Запуск теста
test_generate_report()
print("Все тесты пройдены")
