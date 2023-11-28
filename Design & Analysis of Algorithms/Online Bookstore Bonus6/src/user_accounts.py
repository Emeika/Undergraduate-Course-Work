class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserAccounts:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def get_user_details(self, username):
        return self.users.get(username)
