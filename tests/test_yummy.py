"""script to test users module in app"""
import unittest

from app.users import User
from app.users import userList

class YummyRecipeTests(unittest.TestCase):
    """test class for users"""

    def setUp(self):
        self.new_user = User()
        self.current_user = userList
        self.user_email = "me@me.com"
        self.username = "me"
        self.password = "meawww"
        self.test_user = self.new_user.add_user(self.user_email,self.username,self.password)

    def test_user_created(self):
        """test if user has been created"""
        self.assertTrue(self.user_email in self.test_userList.keys())

    def test_duplicate_user(self):
        duplicate_user = self.new_user.add_user(self.user_email,"mimi","pass123")
        self.assertEqual(duplicate_user,"The email is already in use.")