import random
from Database import check_account_exists_in_db

class Account:
    def __init__(self, name, phn_no, email, balance):
        self.__acc_holder_name = name
        self.__acc_holder_phn = phn_no
        self.__acc_holder_email = email
        self.__account_balance = balance
        self.__account_number = self.generate_account_number()

    # getters
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

def account_create(user_id, initial_balance):

    if check_account_exists_in_db(user_id):
        print("Account already exists.")
    else:
        # Assuming `user_details` is fetched based on `user_id`
        user_details = get_user_details_from_db(user_id)  # Example function to get user details
        if user_details:
            new_account = Account(
                name=user_details['name'],
                phn_no=user_details['phone'],
                email=user_details['email'],
                balance=initial_balance
            )
            # Here you would insert the new account into the database
            insert_account_to_db(new_account)  # Example function to insert account
            print(f"Account created successfully for {new_account.get_acc_holder_name()} with account number {new_account.get_account_number()}")
        else:
            print("User details not found. Account creation failed.")


    

def insert_account_to_db(account):
    # Example function to insert account into the database
    # This function should be implemented in your Database module
    pass
