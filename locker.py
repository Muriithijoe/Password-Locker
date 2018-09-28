class User:
    '''
    class for passing all instances of the user
    '''

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



