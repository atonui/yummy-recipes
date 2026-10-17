"""class to manage user recipes"""

RECIPELIST = []

class Recipes():
    """module to initialise recipe"""
    def __init__(self, title, ingredients, directions):
        self.title = title
        self.ingredients = ingredients
        self.directions = directions
        RECIPELIST.append({"title":self.title, "ingredients":self.ingredients, "directions":self.directions})
