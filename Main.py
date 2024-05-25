import sys
from rich.console import Console

def main():
    try:
        console = Console()
        console.print("\n[bold green]\t\t\t*********** WELCOME TO THE PROJECT **********[/bold green]\n")

        from Menu import main_menu
        main_menu()
    except KeyboardInterrupt:
        console.print("\nExiting the program...")
        sys.exit(0)

if __name__ == '__main__':
    main()
