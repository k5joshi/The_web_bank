import random
from Database import insert_only_balance_in_account
class Bank:
    Bank_name = "THE WEB BANK"
    
    def __init__(self, full_name, phone_number,initial_amount):
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
        # Generate a 10-digit random number
        random_number = random.randint(10**9, (10**10)-1)
        # Add a leading '314' to ensure the number is 14 digits
        account_num = f'314{random_number}'
        return account_num
    
    
    def deposit_money(self,account_number, amount):
        balance = (self.get_balance()+ amount)
        self.set_balance(balance)
        if insert_only_balance_in_account(account_number, self.get_balance()):
            print (f" the amount rs{amount} is credited to you bank account {account_number}, final balance is{ self.get_balance()} ")


    def withdraw_money(self,account_number, amount):
        curr_balance = self.get_balance()
        if curr_balance <= 1000 and amount < 500:
            print("this transaction is declined by the bank try CHECKING THE BALANCE FIRST ")
        else:
            balance = (curr_balance - amount)
            self.set_balance(balance)

            if insert_only_balance_in_account(account_number, self.get_balance()):

                print (f" the amount rs{amount} is debited from your bank account {account_number}, final balance is{ self.get_balance()} ")

    

    

def acc_creation():

    full_name = input("Enter your Full Name: ")
    phone_number = int(input("Enter your phone Number: "))
    initial_amount = int(input("Enter the amount for the initial deposit **(only in integer value **): "))
    
    from Validation import validate_phone_number
    if validate_phone_number(phone_number) == True:

        new_acc = Bank(full_name, 
                      phone_number,
                      initial_amount)

        from Database import insert_acc_into_db
       
            
        insert_acc_into_db(new_acc.get_account_number(),
                           new_acc.get_full_name(),
                           new_acc.get_phone_number(),
                           new_acc.get_balance()
                          )
        print(f"ACCOUNT CREATED SUCCESSFULLY!! {new_acc.get_account_number()} of {new_acc.get_full_name()} is being created in {Bank.Bank_name}")

    