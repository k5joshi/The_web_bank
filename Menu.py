
from Auth import login, signup
def login_menu(username):
    print(f"\n\n WELCOME {username} \n\n")


    while True:
        
        print("PRESS '1' --> to CREATE an ACCOUNT")
        print("PRESS '2' --> to CHECK an ACCOUNT BALANCE")
        print("PRESS '3' --> to WITHDRAW FROM ACCOUNT")
        print("PRESS '4' --> to DEPOSIT MONEY in your ACCOUNT")
        print("PRESS '5' --> to know your account number")
        print("PRESS '11' --> to LOG OUT \n")
        print("PRESS '000' --> to exit ")

        print("choose an option \n")
        choice = input(" Enter your choice: ")

        match choice:
            case '1':
                from Bank_account import acc_creation
                acc_creation()
                

            case '2':
                from Bank_account import Bank
                acc_number = int(input("enter your account number: "))
                pin = input("please enter your PIN : ")

                print( f"\n\n\n BALANCE FETCHED SUCCESSFULLY \n \t\t\tThe balance of **account number : {acc_number} ** is  **Rs {Bank.get_balance_of_account(acc_number, pin)} **\n\n")
                
            case '3':
                from Bank_account import Bank
                acc_num = int(input("enter your account number :"))
                amount = int(input("Enter the amount to withdraw: "))     
                pin = input("please enter your PIN : ")
                
                Bank.withdraw_money(acc_num, amount, pin)
            case '4':
                from Bank_account import Bank
                acc_num = int(input("enter your account number :"))
                amount = int(input("Enter the amount to deposit: "))
                pin = input("please enter your PIN : ")

                Bank.deposit_money(acc_num, amount,pin)
            case '5':
                from Bank_account import Bank
                
                username = input("enter your username: ")
                password = input("enter your password: ")

                Bank.get_account_number_of_user(username, password)
                
            case '11':
                print("\n********** \t \tlogged out successfully\t \t ********** \n")
                main_menu(login, signup)

            case '000':
                print("cancelling the events")
                break
            case _:
                print("invalid input, re-enter the input")


def main_menu(login, signup):
    while True:

        print("\n\n PRESS 1 --> to log in ")
        print(" PRESS 2 --> to signup in the program ")    
        print(" PRESS 0 --> to exit the program \n\n")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                login()

            case '2':
                signup()
            
            case '0':
                print(" CLOSING THE PROGRAM ")
                break
            case _:
                print("invalid input PLEASE RE-ENTER A VALID CHOICE **")
        
        