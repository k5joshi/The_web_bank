

def main():
    from Auth import login, signup
    print(" \t\t\t*********** WELCOME TO THE PROJECT **********")

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

if __name__ == '__main__':
    main()
