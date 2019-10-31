import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
       self.new_user = User(password = 'banana')
   def test_password_setter(self):
       self.assertTrue(self.new_user.pass_secure is not None)
def test_no_access_password(self):
           with self.assertRaises(AttributeError):
               self.new_user.password
def test_password_verification(self):
   self.assertTrue(self.new_user.verify_password('banana'))

class TestArticles(unittest.TestCase):
      '''
   Test class that defines test cases for the contact class behaviours.
   Args:
       unittest.TestCase: TestCase class that helps in creating test cases
   '''
   def setUp(self):
       '''
       Set up method to run before each test cases.
       '''
       self.new-article = Article("1","be yourself","2","10")
  
    def test_init(self):
       '''
       test_init test case to test if the object is initialized properly
       ''' 