class UserSession:
    def __init__(self, user):
        self.current_user = user

    def get_user_info(self):
        return f"Current user: {self.current_user}"

    def end_session(self):
        self.current_user = None
        print("Session ended")
