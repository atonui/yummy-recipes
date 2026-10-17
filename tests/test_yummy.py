"""script to test users module in app"""
import unittest

from app.users import Users
from app.users import USERLIST

class YummyRecipeTests(unittest.TestCase):
    """test class for users"""

    def setUp(self):
        self.current_user = USERLIST
        self.user_email = "me@me.com"
        self.username = "me"
        self.password = "meawww"
        self.name = "Ni Mimi"
        self.new_user = Users(self.user_email, self.password, self.username, self.name)
        self.test_user = self.new_user.add_user(self.user_email, self.password, self.username, self.name)

    def test_user_created(self):
        """test if user has been created"""
        self.assertTrue(self.user_email in self.test_user)
        