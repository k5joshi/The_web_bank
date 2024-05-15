
def login_menu(username):
    print(f"\n\n WELCOME {username} \n\n")


    while True:
        
        print("PRESS '1' --> to CHECK an ACCOUNT BALANCE")
        print("PRESS '2' --> to WITHDRAW FROM ACCOUNT")
        print("PRESS '00' --> to CREATE an ACCOUNT")
        print("PRESS '3' --> to DEPOSIT MONEY in your ACCOUNT")
        print("PRESS '11' --> to LOG OUT \n")

        print("choose an option \n")
        choice = input(" Enter your choice: ")

        match choice:
            case '1':
                print("ok CHECK")
                pass
            case '2':
                print("ok withdraw")
                pass
            case '00':
                print("ok create")
                pass
            case '3':
                print("ok deposit")
                pass
            case '11':
                print("ok logout")
                pass
            case _:
                print("invalid input, re-enter the input")


def main_menu(login, signup):
    while True:

        print("\n\n PRESS 1 --> to log in ")
        print("PRESS 2 --> to signup in the program ")    
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
        
        