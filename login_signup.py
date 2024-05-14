
from User import User
from Validation import password_validation

def login():

    print("\n please enter the details to get logged in \n")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

def signup():
    while True:
        username = input("Enter the username: ")
        password = input("Type a strong password: ")
        re_password = input("Re-enter the password: ")

        if password_validation(password, re_password):
            # If password is valid, create a User instance and set username and password
            new_user = User(username, password)
            User.user_creation(new_user.get_username(), new_user.get_password())
            break
        else:
            # If password is invalid, prompt the user to try again
            print("Password not acceptable. Please try again.")


