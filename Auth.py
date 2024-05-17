from User import User
from Validation import password_validation, input_date_of_birth, validate_phone_number, validate_email

def login():
    print("\nPlease enter the details to get logged in\n")
    input_username = input("Enter the username: ")
    input_password = input("Enter the password: ")

    # Check if either input is empty
    if input_username == '' or input_password == '':
        print("Empty inputs")
        from Main import main  # Importing main() from the correct module
        main()
    else:
        from Database import check_data_from_db # Ensure pass_args is imported from the correct module
        check_data_from_db(input_username, input_password)



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
        full_name = input("Enter your full name: ")
        phone_number = int(input("Enter your phone number: "))
        email = input("Enter your Email: ")
        date_of_birth = input_date_of_birth()

        if password_validation(password, re_password) and validate_phone_number(phone_number) and validate_email(email) == True:
            # If password is valid, create a User instance and set username and password

            new_user = User(username,
                            password,
                            full_name ,
                            phone_number,
                            email,
                            date_of_birth)
            
            User.user_creation(new_user.get_username(),
                               new_user.get_password(),
                               new_user.get_full_name() ,
                               new_user.get_phone_number(),
                               new_user.get_email(),
                               new_user.get_date_of_birth())
            break
        else:
            # If password is invalid, prompt the user to try again
            print(" Please try again.")
