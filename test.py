import pyperclip
import unittest
from locker import User
from credential import Credential

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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Joe")
        self.assertEqual(self.new_user.account_name,"Instagram")
        self.assertEqual(self.new_user.email,"@joe.com")
        self.assertEqual(self.new_user.password,"killshot18")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple users object to our lists
        '''
        self.new_user.save_user()
        test_user = User("Roman","Facebook","@roman.com","reigns18")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("Roman","Facebook","@roman.com","reigns18")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_account_name(self):
        '''
        test to check if we can find user by account name and display information
        '''
        self.new_user.save_user()
        test_user = User("Roman","Facebook","@roman.com","reigns18")
        test_user.save_user()

        found_user = User.find_by_account_name("Facebook")
        self.assertEqual(found_user.password,test_user.password)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if cannot find the contact.
        '''
        self.new_user.save_user()
        test_user = User("Roman","Facebook","@roman.com","reigns18")
        test_user.save_user()

        user_exists = User.user_exist("Facebook")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all contacts saved
        '''
        self.assertEqual(Credential.display_users(),Credential.user_list)

    def test_copy_email(self):
        '''
        test to confirm that we are copying email from found user
        '''
        self.new_user.save_user()
        User.copy_email("Instagram")

        self.assertEqual(self.new_user.email,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()