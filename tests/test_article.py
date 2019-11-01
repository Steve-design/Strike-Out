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
   Test class that defines test cases for the article class behaviours.
   Args:
       unittest.TestCase: TestCase class that helps in creating test cases
   '''
   def setUp(self):
       '''
       Set up method to run before each test cases.
       '''
       self.new_article = Article("1","be yourself","2","10")
  
    def test_init(self):
       '''
       test_init test case to test if the object is initialized properly
       ''' 
       self.assertEqual(self.new_article.id,"1")
       self.assertEqual(self.new_article.content,"be yourself")
       self.assertEqual(self.new_article.category_id,"2")
       self.assertEqual(self.new_article.user_id,"10")

    def test_save_article(self):
       '''
       test_save_article test case to test if the article object is saved
       '''
    self.new_article.save_article()
    self.assertEqual(len(Article.article_list),1)

if __name__ == '__main__':
   unittest.main() 