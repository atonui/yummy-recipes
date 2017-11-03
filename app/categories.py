"""class to manage user categories"""
from .recipes import Recipes

CATEGORYLIST = []

class Categories(object):
    """module to initialise recipe"""
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.recipes = []
       
