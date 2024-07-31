class SMTPClient:
    def send(self, to, subject, body):
        print(f"Sending email to {to}: {subject}\n{body}")

class EmailSender:
    def __init__(self):
        self.smtp_client = None  # Инициализация пустым значением

    def get_smtp_client(self):
        if self.smtp_client is None:
            self.smtp_client = SMTPClient()  # Логика создания объекта
        return self.smtp_client

    def send_notification(self, to, subject, body):
        self.get_smtp_client().send(to, subject, body)  # Использование получателя

class MockSMTPClient:
    def send(self, to, subject, body):
        print(f"Mock sending email to {to}: {subject}\n{body}")

class TestEmailSender(EmailSender):
    def get_smtp_client(self):
        if self.smtp_client is None:
            self.smtp_client = MockSMTPClient()  # Использование фиктивного объекта
        return self.smtp_client

# Пример использования
email_sender = EmailSender()
email_sender.send_notification("user@example.com", "Welcome!", "Thank you for signing up!")

# Пример использования тестирующего подкласса
test_email_sender = TestEmailSender()
test_email_sender.send_notification("user@example.com", "Welcome!", "Thank you for signing up!")
