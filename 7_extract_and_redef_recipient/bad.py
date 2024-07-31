class SMTPClient:
    def send(self, to, subject, body):
        print(f"Sending email to {to}: {subject}\n{body}")

class EmailSender:
    def __init__(self):
        self.smtp_client = SMTPClient()  # Объект, который требуется извлечь

    def send_notification(self, to, subject, body):
        self.smtp_client.send(to, subject, body)  # Прямое использование объекта

# Пример использования
email_sender = EmailSender()
email_sender.send_notification("user@example.com", "Welcome!", "Thank you for signing up!")
