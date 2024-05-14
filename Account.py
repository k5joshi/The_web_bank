import random 

class Account:

    def __init__(self, name, phn_no, email, balance):
        self.__acc_holder_name = name
        self.__acc_holder_phn = phn_no
        self.__acc_holder_email = email
        self.__acccount_balance = balance
        self.__account_number = self.generate_account_number()


    #getters
    def get_acc_holder_name(self):
        return self.__acc_holder_name

    def get_acc_holder_phn(self):
        return self.__acc_holder_phn

    def get_acc_holder_email(self):
        return self.__acc_holder_email

    def get_account_balance(self):
        return self.__acccount_balance

    def get_account_number(self):
        return self.__account_number

    # setters
    def set_acc_holder_name(self, name):
        self.__acc_holder_name = name
    
    def set_acc_holder_phone(self, phone_number):
        self.__acc_holder_phn = phone_number
    
    def set_acc_holder_email(self, email):
        self.__acc_holder_email = email

    def set_acc_holder_balance(self, balance):
        self.__account_balance = balance
    


    def generate_account_number(self):
        # Generate a 10-digit random number
        random_number = random.randint(10**9, (10**10)-1)
        # Add a leading '314' to ensure the number is 14 digits
        account_num = int('314' + str(random_number))
        return account_num


account_1 = Account ("kartik",9720438537,"kartikjoshi842003@gmail.com",4000)
print(account_1.get_account_number())