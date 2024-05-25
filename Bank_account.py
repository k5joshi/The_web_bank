import random
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

console = Console()

class Bank:
    Bank_name = "THE WEB BANK"
    
    def __init__(self, full_name, phone_number, pin, initial_amount):
        self.__account_num = self.generate_account_number()
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__balance = initial_amount
        self.__pin = pin

    def get_account_number(self):
        return self.__account_num
    
    def get_full_name(self):
        return self.__full_name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance
    
    def set_full_name(self, full_name):
        self.__full_name = full_name
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_pin(self, pin):
        self.__pin = pin
        
    def set_balance(self, amount):
        self.__balance = amount

    def generate_account_number(self):
        random_number = random.randint(10**9, (10**10)-1)
        account_num = f'314{random_number}'
        return account_num

    def input_pin(self):
        console.print(Panel("CREATE A 4 DIGIT PIN FOR YOUR ACCOUNT TRANSACTIONS\n** DON'T SHARE IT WITH ANYONE **", title="PIN Creation", style="bold yellow"))

        while True:
            pin = Prompt.ask("Please enter a 4-digit PIN")
            if pin.isdigit() and len(pin) == 4:
                return int(pin)
            else:
                console.print("[bold red]PIN must be a 4-digit integer.[/bold red]")

    @staticmethod
    def get_balance_of_account(account_number, pin):
        from Database import get_account_details
        account_details = get_account_details(account_number, pin)
        return account_details['balance']

    @staticmethod
    def deposit_money(account_num, amount, pin):
        from Database import get_update_account_balance, get_account_details
        user_account = get_account_details(account_num, pin)

        if user_account["account_number"] == account_num:
            balance = Bank.get_balance_of_account(account_num, pin)
            new_balance = balance + amount
            get_update_account_balance(account_num, new_balance, pin)
            console.print(f"[bold green]Amount of Rs {amount} is credited to your account {account_num}. Final balance is Rs {Bank.get_balance_of_account(account_num, pin)}.[/bold green]")
        else:
            console.print("[bold red]You are not authorized to access this account.[/bold red]")

    @staticmethod
    def withdraw_money(account_num, amount, pin):
        from Database import get_update_account_balance, get_account_details
        user_account = get_account_details(account_num, pin)

        if user_account["account_number"] == account_num:
            balance = Bank.get_balance_of_account(account_num, pin)
            if balance >= 1000 and amount <= balance - 1000 and amount >= 500:
                new_balance = balance - amount
                get_update_account_balance(account_num, new_balance, pin)
                console.print(f"[bold green]The amount {amount} is debited from your account {account_num}. Final balance is Rs {Bank.get_balance_of_account(account_num, pin)}.[/bold green]")
            else:
                console.print("[bold red]Please check your account balance or the withdrawal amount. Minimum withdrawal amount is Rs 500.[/bold red]")
        else:
            console.print("[bold red]You are not authorized to access this account.[/bold red]")

    @staticmethod
    def get_account_number_of_user(username, password):
        try:
            from Database import get_user_accounts
            account_num = get_user_accounts(username, password)
            console.print(f"[bold green]The bank account associated with {username} is {account_num}.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error in get_account_number_of_user: {e}[/bold red]")

def acc_creation():
    full_name = Prompt.ask("Enter your Full Name")
    phone_number = Prompt.ask("Enter your phone Number")
    pin = Bank(full_name, phone_number, None, None).input_pin()
    initial_amount = int(Prompt.ask("Enter the amount for the initial deposit (only in integer value)"))

    from Validation import validate_phone_number
    if validate_phone_number(phone_number):
        new_acc = Bank(full_name, phone_number, pin, initial_amount)

        username = Prompt.ask("Enter your username for the account creation")
        password = Prompt.ask("Enter your password for account creation", password= True)
        from Database import insert_acc_into_db, get_user_id_of_user_from_db
        user_id = get_user_id_of_user_from_db(username, password)

        insert_acc_into_db(new_acc.get_account_number(), user_id, new_acc.get_full_name(), new_acc.get_phone_number(), new_acc.get_pin(), new_acc.get_balance())

        console.print(f"[bold green]ACCOUNT CREATED SUCCESSFULLY!!\nAccount Number: {new_acc.get_account_number()} of {new_acc.get_full_name()} is created in {Bank.Bank_name}[/bold green]")
    else:
        console.print("[bold red]Invalid phone number. Please try again.[/bold red]")
