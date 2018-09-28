class Credential:
    '''
    class generates all instances of credentials
    '''

    user_list = []

    def delete_user(self):
        '''
        delete_user method delete a saved user from user_list
        '''
        Credential.user_list.remove(self)

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
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list







