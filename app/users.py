"""user management script"""
from .recipes import Recipes
USERLIST = []

class Users():
    def __init__(self, email, password, username, name):
        self.email = email
        self.password = password
        self.username = username
        self.name = name
        self.category=[]

    def create_category(self, category):
        self.category.append(category)
        return 'Category added!'

    #def current_User(self):
        #return currentUser = USERLIST[-1]
        
    def add_user(self, email, password, username, name):
         for item in USERLIST:
             if email not in item["email"]:
                 USERLIST.append({"email":email,"password":password,"username":username,"name":name})
                 return True
             else:
                 return False

    # def fetch_user(self, email, password):
    #     for item in USERLIST:
    #         if email in item["email"] and password in item["password"]:
    #             return True
    #         else:
    #             return False

    def add_recipe(self, recipeTitle, categoryName):
        self.category["title"] = recipeTitle
        self.category["category"] = categoryName

