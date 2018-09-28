class User:
    '''
    class for passing all instances of the user
    '''

    def __init__(self,username,account_name,email,password):
        '''
        initiates properties of my objects

        Args:
            username:New username of the account
            account_name:New account name
            email:New email address
            password:New password
        '''
        self.username = username
        self.account_name = account_name
        self.email = email
        self.password = password

        

