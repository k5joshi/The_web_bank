from User import User
from Validation import password_validation, input_date_of_birth, validate_phone_number, validate_email
from Database import check_user_in_db
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import hashlib

console = Console()

def login():
    console.print(Panel(Text("Please enter the details to get logged in", justify="center", style="bold green")))

    input_username = Prompt.ask("Enter the username", default="")
    input_password = Prompt.ask("Enter the password", default="",show_default=False, password=True)

    if input_username == '' or input_password == '':
        console.print("[bold red]Empty inputs[/bold red]")
        from Main import main  # Importing main() from the Main module;p
        main()
    else:
        check_user_in_db(input_username, input_password)

def signup():
    console.print(Panel(Text("NOTE: PASSWORD rules to STRONG password:\n"
                            "1. LENGTH SHOULD BE > 10\n"
                            "2. AT LEAST ONE UPPERCASE AND ONE LOWERCASE\n"
                            "3. AT LEAST ONE SPECIAL CHARACTER\n"
                            "4. AT LEAST ONE DIGIT FROM 0 TO 9", justify="left", style="bold yellow"), 
                            title="Password Rules", title_align="center"))

    while True:
        username = Prompt.ask("Enter the username")
        password = Prompt.ask("Type a strong password", password=True)
        re_password = Prompt.ask("Re-enter the password", password=True)
        full_name = Prompt.ask("Enter your full name")
        phone_number = Prompt.ask("Enter your phone number", default="")
        email = Prompt.ask("Enter your Email")
        date_of_birth = input_date_of_birth()

        if password_validation(password, re_password) and validate_phone_number(phone_number) and validate_email(email):
            new_user = User(username, password, full_name, phone_number, email, date_of_birth)
            User.user_creation(new_user.get_username(),
                               new_user.get_password(),
                               new_user.get_full_name(),
                               new_user.get_phone_number(),
                               new_user.get_email(),
                               new_user.get_date_of_birth())
            console.print("[bold green]User created successfully![/bold green]")
            break
        else:
            console.print("[bold red]Please try again.[/bold red]")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
