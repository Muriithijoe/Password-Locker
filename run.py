#!/usr/bin/env python3.6

from locker import User
from credential import Credential

def create_user(uname,account,email,password):
    '''
    function to create a new user
    '''
    new_user = User(uname,account,email,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(account_name):
    '''
    Function for returning user
    '''
    return User.find_by_account_name(account_name)

def check_existing_user(account_name):
    '''
    Function that check if a user exists
    '''
    return User.user_exist(account_name)

def display_user():
    '''
    Function returns all saved users
    '''
    return User.display_user()

def main():
    print("Hello Welcome to your Password-Locker. What is your name ? ")
    user_name =input()
    print(f"Hello {user_name}.what would you like to do ?")
    print('\n')
    while True:
        print("Use these short codes: cu - create a new user, du - display user, fu - find a user, ex - exit the user")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print("Username ....")
            u_name = input()

            print("Account ...")
            account_name = input()

            print("Email Address ...")
            e_address = input()

            print("Password ...")
            password = input()

            save_user(create_user(u_name,account_name,e_address,password))

            print('\n')
            print(f"New User {u_name} created")
            print('\n')

        elif short_code == 'du':
            if display_user():
                print("Here are all the users")
                print('\n')
                for user in display_user():
                    print(f"{user.user_name}......{user.account_name}")

                print('\n')

            else:
                print('\n')
                print("You dont seem to have any users yet")
                print('\n')

        elif short_code == "fu":
            print("Enter the where Account is")
            search_acccout_name = input()
            if check_existing_user(search_acccout_name):
                search_acccout_name = find_user(search_acccout_name)
                print(f"{search_acccout_name.user_name}")
                print('-' * 20)
                print(f"{search_acccout_name.account_name}")
                print(f"{search_acccout_name.password}")
            else:
                print("That User does not exist")


if __name__ == '__main__':
    main()