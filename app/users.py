"""user management script"""
userList = {}

class Users(object):
    def __init__(self, email=None,username=None,password=None):
        self.email = email
        self.username = username
        self.password = password