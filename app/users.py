"""user management script"""
USERLIST = []

class Users(object):
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
        

    def add_user(self, email, password):
        global USERLIST
        for item in USERLIST:
            if email not in item['emailAddress']:
                USERLIST.append({"emailAddress":email,"passwordValue":password})
                return True
        else:
            return False

    def fetch_user(self, email=None, password=None,):
        for item in USERLIST:
            if item["emailAddress"] == email and item["passwordValue"] == password:
                return True
            else:
                return False
                break