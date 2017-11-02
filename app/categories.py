"""class to manage user categories"""

CATEGORYLIST = []

class Categories():
    """module to initialise recipe"""
    def __init__(self, title, recipes):
        self.title = title
        self.recipes = {}
       
