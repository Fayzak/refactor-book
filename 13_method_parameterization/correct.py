class EmailService:
    def send_email(self, to, subject, body):
        print(f"Sending email to {to}: {subject} - {body}")

class MockEmailService(EmailService):
    def send_email(self, to, subject, body):
        print(f"[MOCK] Sending email to {to}: {subject} - {body}")

class ReportGenerator:
    def generate_and_send_report(self, recipient, email_service=None):
        report = "This is the report content."
        if email_service is None:
            email_service = EmailService()
        email_service.send_email(recipient, "Monthly Report", report)

    def generate_and_send_report_default(self, recipient):
        self.generate_and_send_report(recipient, EmailService())

# Пример использования
report_generator = ReportGenerator()
report_generator.generate_and_send_report_default("user@example.com")  # Вывод: "Sending email to user@example.com: Monthly Report - This is the report content."

# Использование mock-версии для тестирования
mock_email_service = MockEmailService()
report_generator.generate_and_send_report("user@example.com", mock_email_service)  # Вывод: "[MOCK] Sending email to user@example.com: Monthly Report - This is the report content."
