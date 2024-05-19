import random
import sqlite3

class Bank:
    Bank_name = "THE WEB BANK"
    
    def __init__(self, full_name, phone_number, initial_amount):
        self.__account_num = self.generate_account_number()
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__balance = initial_amount

    def get_account_number(self):
        return self.__account_num
    
    def get_full_name(self):
        return self.__full_name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_balance(self):
        return self.__balance
    
    def set_full_name(self, full_name):
        self.__full_name = full_name
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_balance(self, amount):
        self.__balance = amount

    def generate_account_number(self):
        random_number = random.randint(10**9, (10**10)-1)
        account_num = f'314{random_number}'
        return account_num
    
    @staticmethod
    def get_balance_of_account(account_number):
        from Database import get_account_details
        account_details = get_account_details(account_number)
        return account_details['balance']

    @staticmethod
    def deposit_money(user_id, account_num, amount):
        from Database import get_update_account_balance, get_account_owner_id
        owner_id = get_account_owner_id(account_num)
        if owner_id == user_id:
            balance = Bank.get_balance_of_account(account_num)
            new_balance = balance + amount
            get_update_account_balance(account_num, new_balance)
            print(f" \n \t\t\tamount of Rs {amount} is credited to your account {account_num} final balance is {Bank.get_balance_of_account(account_num)}\n\n")
        else:
            print("You are not authorized to access this account.")
        
    @staticmethod
    def withdraw_money(user_id, account_num, amount):
        from Database import get_update_account_balance, get_account_owner_id
        owner_id = get_account_owner_id(account_num)
        if owner_id == user_id:
            balance = Bank.get_balance_of_account(account_num)
            if balance >= 1000 and amount <= balance - 1000 and amount >= 500:
                new_balance = balance - amount
                get_update_account_balance(account_num, new_balance)
                print(f"\n \tthe amount {amount} is debited from your account {account_num} final balance is {Bank.get_balance_of_account(account_num)}\n\n")
            else:
                print("Please check your account balance or the withdrawal amount. Minimum withdrawal amount is Rs 500.")
        else:
            print("You are not authorized to access this account.")




def acc_creation():
    full_name = input("Enter your Full Name: ")
    phone_number = input("Enter your phone Number: ")
    initial_amount = int(input("Enter the amount for the initial deposit (only in integer value): "))
    
    from Validation import validate_phone_number
    if validate_phone_number(phone_number):
        new_acc = Bank(full_name, phone_number, initial_amount)
        from Database import insert_acc_into_db
        
        insert_acc_into_db(new_acc.get_account_number(), new_acc.get_full_name(), new_acc.get_phone_number(), new_acc.get_balance())
        
        print(f"\n\n ACCOUNT CREATED SUCCESSFULLY!! Account Number: {new_acc.get_account_number()} of {new_acc.get_full_name()} is created in {Bank.Bank_name}\n\n")
    else:
        print("Invalid phone number. Please try again.")

