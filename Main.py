from Menu import main_menu

def main():
    from Auth import login, signup
    print(" \t\t\t*********** WELCOME TO THE PROJECT **********")

    main_menu(login, signup)

if __name__ == '__main__':
    main()
