"""user management script"""
from .recipes import Recipes
USERLIST = []

class Users(object):
    def __init__(self, email, password, username, name):
        self.email = email
        self.password = password
        self.username = username
        self.name = name
        USERLIST.append({"email":self.email,"password":self.password,"username":self.username,"name":self.name})
        self.category={}
        
    def add_user(self, email, password, username, name):
        for item in USERLIST:
            if email not in item["email"]:
                USERLIST.append({"email":email,"password":password,"username":username,"name":name})
                return True
            else:
                return False

    def fetch_user(self, email, password):
        for item in USERLIST:
            if email in item["email"] and password in item["password"]:
                return True
            else:
                return False

    def add_recipe(self, recipeTitle, categoryName):
        self.category["title"] = recipeTitle
        self.category["category"] = categoryName

    def fetch_recipe(self, title):
        if title in self.recipe:
            return True
