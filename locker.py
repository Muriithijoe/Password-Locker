import pyperclip
class User:
    '''
    class for passing all instances of the user
    '''

    user_list = []

    def __init__(self,user_name,account_name,email,password):
        '''
        initiates properties of my objects

        Args:
            user_name:New username of the account
            
        '''
        self.user_name = user_name
        self.account_name = account_name
        self.email = email
        self.password = password

        

    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method delete a saved user from user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method takes account name and returns password that matches that account

        Args:
            number: Phone number to search for
        Returns:
            Contact of person that matches the number
        '''

        for user in cls.user_list:
            if user.account_name == account_name :
                return user

    @classmethod
    def user_exist(cls,account_name):
        '''
        Method that checks if a contact exists from contact lists.
        Args:
            number: account name to search if it exists
        Returns:
            Boolean: True or False depending if the contact exists
        '''
        for user in cls.user_list:
            if user.account_name == account_name:
                return True

        return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls,account_name):
        user_found = User.find_by_account_name(account_name)
        pyperclip.copy(user_found.email)
        






