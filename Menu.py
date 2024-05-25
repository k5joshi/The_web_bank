from Auth import login, signup
from rich.console import Console
from rich.table import Table
from rich import print
from rich.prompt import Prompt
console = Console()

def login_menu(username):
    console.print(f"\n\n [bold green]WELCOME {username}[/bold green] \n\n")

    while True:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Description", style="dim")

        table.add_row("1", "CREATE an ACCOUNT")
        table.add_row("2", "CHECK an ACCOUNT BALANCE")
        table.add_row("3", "WITHDRAW FROM ACCOUNT")
        table.add_row("4", "DEPOSIT MONEY in your ACCOUNT")
        table.add_row("5", "Know your ACCOUNT NUMBER")
        table.add_row("11", "LOG OUT")
        table.add_row("000", "Exit")

        console.print(table)
        choice = Prompt.ask("[bold yellow] Enter your choice: [/bold yellow]")

        match choice:
            case '1':
                from Bank_account import acc_creation
                acc_creation()

            case '2':
                from Bank_account import Bank
                acc_number = int(console.input("[bold cyan]Enter your account number: [/bold cyan] "))
                pin = console.input("[bold cyan]Please enter your PIN: [/bold cyan] ")

                balance = Bank.get_balance_of_account(acc_number, pin)
                console.print(f"\n\n\n [bold green]BALANCE FETCHED SUCCESSFULLY[/bold green] \n\t\t\tThe balance of [bold]account number: {acc_number}[/bold] is [bold]Rs {balance}[/bold]\n\n")

            case '3':
                from Bank_account import Bank
                acc_num = int(console.input("[bold cyan]Enter your account number: [/bold cyan] "))
                amount = int(console.input("[bold cyan]Enter the amount to withdraw: [/bold cyan] "))
                pin = console.input("[bold cyan]Please enter your PIN: [/bold cyan] ")

                Bank.withdraw_money(acc_num, amount, pin)

            case '4':
                from Bank_account import Bank
                acc_num = int(console.input("[bold cyan]Enter your account number: [/bold cyan] "))
                amount = int(console.input("[bold cyan]Enter the amount to deposit: [/bold cyan] "))
                pin = console.input("[bold cyan]Please enter your PIN: [/bold cyan] ")

                Bank.deposit_money(acc_num, amount, pin)

            case '5':
                from Bank_account import Bank

                username = console.input("[bold cyan]Enter your username: [/bold cyan] ")
                password = console.input("[bold cyan]Enter your password: [/bold cyan] ")

                Bank.get_account_number_of_user(username, password)

            case '11':
                console.print("\n[bold green]********** Logged out successfully **********[/bold green]\n")
                main_menu(login, signup)
                break

            case '000':
                console.print("[bold red]Cancelling the events[/bold red]")
                exit()

            case _:
                console.print("[bold red]Invalid input, please re-enter the input[/bold red]")

def main_menu():
    while True:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Description", style="dim")

        table.add_row("1", "Log in")
        table.add_row("2", "Sign up in the program")
        table.add_row("0", "Exit the program")

        console.print(table)
        choice = Prompt.ask("[bold yellow]Enter your choice:[/bold yellow]")

        match choice:
            case '1':
                login()

            case '2':
                signup()

            case '0':
                console.print("[bold red]CLOSING THE PROGRAM[/bold red]")
                exit()

            case _:
                console.print("[bold red]Invalid input, please re-enter a valid choice[/bold red]")


def main():
    main_menu()

if __name__ == "__main__":
     main()
