import unittest

class YummyRecipeTests(unittest.TestCase):

    def test_user_created(self):
        """test if user has been created"""
        self.assertTrue(self.user_email in self.test_user.keys())