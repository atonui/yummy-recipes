"""user management script"""
USERLIST = {}

class User(object):
    def __init__(self, email=None, username=None, password=None):
        self.email = email
        self.username = username
        self.password = password

    def add_user(self, email, username, password):
        if email not in USERLIST:
            USERLIST[email] = {"email":email, "username":username, "password":password}
            return USERLIST
        else:
            return "The email address is already in use."

    def fetch_user(self, email=None, password=None, users=None):
        if email in USERLIST:
            current_user = USERLIST[email]
            if current_user["password"] == password:
                return current_user
            else:
                return "Non existent user"
