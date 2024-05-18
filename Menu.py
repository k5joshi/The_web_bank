
from Auth import login, signup
def login_menu(username):
    print(f"\n\n WELCOME {username} \n\n")


    while True:
        
        print("PRESS '1' --> to CREATE an ACCOUNT")
        print("PRESS '2' --> to CHECK an ACCOUNT BALANCE")
        print("PRESS '3' --> to WITHDRAW FROM ACCOUNT")
        print("PRESS '4' --> to DEPOSIT MONEY in your ACCOUNT")
        print("PRESS '11' --> to LOG OUT \n")

        print("choose an option \n")
        choice = input(" Enter your choice: ")

        match choice:
            case '1':
                from Bank_account import acc_creation
                acc_creation()
                print("\n\n create\n\n")

            case '2':
                print("/n ok CHECK ")
                pass
            case '3':     
                acc_num = int(input("enter the account number: "))
                amount = int(input("enter the amount: "))
                from Bank_account import Bank
                Bank.withdraw_money(acc_num, amount)
                print("ok withdraw")
            case '4':
                acc_num = int(input("enter the account number: "))
                amount = int(input("enter the amount: "))
                from Bank_account import Bank
                Bank.deposit_money(acc_num, amount)
                print("ok deposit")
                
            case '11':
                print("\n********** \t \tlogged out successfully\t \t ********** \n")
                main_menu(login, signup)
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
        
        