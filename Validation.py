from rich.console import Console
import re, datetime

console = Console()

## password validation starts ----
def password_validation(password, re_password):
    # Check length
    if len(password) < 10:
        console.print("\n[bold red]Invalid password: Password must be at least 10 characters long[/bold red]")
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        console.print("\n[bold red]Invalid password: Password must contain at least one uppercase letter[/bold red]")
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        console.print("\n[bold red]Invalid password: Password must contain at least one lowercase letter[/bold red]")
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        console.print("\n[bold red]Invalid password: Password must contain at least one digit[/bold red]")
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    
    if not any(char in special_characters for char in password):
        console.print("\n[bold red]Invalid password: Password must contain at least one special character[/bold red]")
        return False
    
    # Check if password matches re-entered password
    if password != re_password:
        console.print("\n[bold red]Invalid password: Passwords do not match[/bold red]")
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
        console.print("\n[bold red]Invalid date format: Please enter date in YYYY-MM-DD format[/bold red]")
        return False

def input_date_of_birth():
    while True:
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
        if is_valid_date(date_of_birth):
            return date_of_birth

## phone number validation starts-----

def validate_phone_number(phone_number):
    # Regular expression pattern for a typical phone number format
    pattern = r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    
    # Check if the phone number matches the pattern
    if re.match(pattern, str(phone_number)):
        return True
    else:
        console.print("\n[bold red]Invalid phone number: Please enter a valid phone number[/bold red]")
        return False
    
## email validation starts ----- 

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        console.print("\n[bold red]Invalid email address: Please enter a valid email address[/bold red]")
        return False
