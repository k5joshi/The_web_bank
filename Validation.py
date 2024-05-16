
import datetime, re


## password validation starts ----
def password_validation(password, re_password):
    # Check length
    if len(password) < 10:
        print("\ninvalid password")
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("\ninvalid password")
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        print("\ninvalid password")
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        print("\ninvalid password")
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    
    if not any(char in special_characters for char in password):
        print("\ninvalid password")
        return False
    
    # Check if password matches re-entered password
    if password != re_password:
        print("\ninvalid password")
        return False

    # If all conditions pass, return True
    return True



# date validation --starts--

def is_valid_date(date_string):
    try:
        # Attempt to convert the input string to a date
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def input_date_of_birth():
    while True:
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
        if is_valid_date(date_of_birth):
            return date_of_birth
        else:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")



## phone number validation starts-----

def validate_phone_number(phone_number):
    # Regular expression pattern for a typical phone number format
    pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    
    # Check if the phone number matches the pattern
    if re.match(pattern, str(phone_number)):
        return True
    else:
        print("\ninvalid phone number")
        return False
    
## email validation starts ----- 

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        print("\ninvalid email address")
        return False