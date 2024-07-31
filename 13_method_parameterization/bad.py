class EmailService:
    def send_email(self, to, subject, body):
        print(f"Sending email to {to}: {subject} - {body}")

class ReportGenerator:
    def generate_and_send_report(self, recipient):
        report = "This is the report content."
        email_service = EmailService()  # Создание объекта внутри метода
        email_service.send_email(recipient, "Monthly Report", report)

# Пример использования
report_generator = ReportGenerator()
report_generator.generate_and_send_report("user@example.com")
