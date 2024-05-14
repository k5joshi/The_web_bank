from User import User
from Database import check_data
from Main import main
from Validation import password_validation

def login():
    print("\nPlease enter the details to get logged in\n")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username and password:
        check_data(username, password)
    else:
        print("Empty inputs")  
        # Assuming main() is imported from another module
        main()



def signup():

    print('''**\n
            NOTE: PASSWORD rules to STRONG password:
                    1. LENGTH SHOULD BE > 10
                    2. ATLEAST ONE UPPERCASE AND ONE LOWERCASE
                    3. ATLEAST ONE SPECIAL CHARACTER
                    4. ATLEAST ONE DIGIT FROM 0 TO 9
          
                \n**  ''')

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