from Menu import main_menu
from Auth import login, signup

def main():
    print(" \t\t\t*********** WELCOME TO THE PROJECT **********")

    main_menu(login, signup)

if __name__ == '__main__':
    main()
