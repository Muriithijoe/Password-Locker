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
            account_name:New account name
            email:New email address
            password:New password
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






