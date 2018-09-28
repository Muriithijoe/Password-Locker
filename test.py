import unittest
from locker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for user class behaviours

    Args:
        unittest.TestCase: class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Joe","Instagram","@joe.com","killshot18")

    def test_init(self):
        '''
        test_init test case to case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Joe")
        self.assertEqual(self.new_user.account_name,"Instagram")
        self.assertEqual(self.new_user.email,"@joe.com")
        self.assertEqual(self.new_user.password,"killshot18")

if __name__ == '__main__':
    unittest.main()