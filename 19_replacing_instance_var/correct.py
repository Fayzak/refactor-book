class UserSession:
    def __init__(self, user):
        self.current_user = user

    def get_user_info(self):
        return f"Current user: {self.current_user}"

    def end_session(self):
        self.current_user = None
        print("Session ended")

    def supersede_current_user(self, new_user):
        self.end_session()
        self.current_user = new_user
        print(f"User superseded to: {self.current_user}")

# Пример использования
session = UserSession("Alice")
print(session.get_user_info())  # Current user: Alice

session.supersede_current_user("Bob")
print(session.get_user_info())  # Current user: Bob
