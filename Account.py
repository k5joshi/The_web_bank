import random
from Database import check_account_exists_in_db

class Account:
    def __init__(self,key, name, phn_no, email, balance, account_num):
        self.__acc_holder_key = self.set_acc_holder_key()
        self.__acc_holder_name = name
        self.__acc_holder_phn = phn_no
        self.__acc_holder_email = email
        self.__account_balance = balance
        self.__account_number = self.generate_account_number()

    # getters
    def get_acc_holder_key(self):
        return self.__user_key

    def get_acc_holder_name(self):
        return self.__acc_holder_name

    def get_acc_holder_phn(self):
        return self.__acc_holder_phn

    def get_acc_holder_email(self):
        return self.__acc_holder_email

    def get_account_balance(self):
        return self.__account_balance

    def get_account_number(self):
        return self.__account_number

    # setters
    def set_acc_holder_key(self, key):
        self.__acc_holder_key = key

    def set_acc_holder_name(self, name):
        self.__acc_holder_name = name

    def set_acc_holder_phn(self, phn_no):
        self.__acc_holder_phn = phn_no

    def set_acc_holder_email(self, email):
        self.__acc_holder_email = email

    def set_account_balance(self, balance):
        self.__account_balance = balance

def generate_account_number(self):
    # Generate a 10-digit random number
    random_number = random.randint(10**9, (10**10)-1)
    # Add a leading '314' to ensure the number is 14 digits
    account_num = f'314{random_number}'
    return account_num



    
