
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
                

            case '2':
                from Bank_account import Bank
                acc_number = int(input("enter your account number: "))

                print( f"\n\n\n BALANCE FETCHED SUCCESSFULLY \n \t\t\tThe balance of **account number : {acc_number} ** is  **Rs {Bank.get_balance_of_account(acc_number)} **\n\n")
                
            case '3':
                from Bank_account import Bank
                acc_num = int(input("enter your account number :"))
                amount = int(input("Enter the amount to withdraw: "))     
                user_id = int(input("please enter your user pass key *YOUR KEY IS THE ID WHICH IS CREATED WHEN YOUR CREATED YOUR USER ACCOUNT **   :"))
                
                Bank.withdraw_money(user_id,acc_num, amount)
            case '4':
                from Bank_account import Bank
                acc_num = int(input("enter your account number :"))
                amount = int(input("Enter the amount to deposit: "))
                user_key = int(input("please enter your user pass key *YOUR KEY IS THE ID WHICH IS CREATED WHEN YOUR CREATED YOUR USER ACCOUNT **   :"))    

                Bank.deposit_money(user_id,acc_num, amount)
                
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
        
        