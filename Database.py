import sqlite3
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

# Database aur cursor creation
def create_db_and_tables():
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            full_Name TEXT NOT NULL,
            phone_Number TEXT NOT NULL,
            email TEXT NOT NULL,
            date_Of_Birth DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts(
            account_number INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL,
            full_name TEXT NOT NULL,
            phone_number INTEGER NOT NULL,
            pin TEXT NOT NULL, 
            balance INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    connection.commit()
    connection.close()

# Function to insert user into database
def insert_user_to_db(user_id, username, password, full_name, phone_number, email, date_of_birth):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO users (user_id, username, password, full_name, phone_Number, email, date_Of_Birth) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (user_id, username, password, full_name, phone_number, email, date_of_birth))
        connection.commit()
        console.print("[bold green]User successfully inserted into the database.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error in inserting user: {e}[/bold red]")
    finally:
        connection.close()

# Function to insert account into database
def insert_acc_into_db(account_number, user_id, full_name, phone_number, pin, balance):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO accounts (account_number, user_id, full_name, phone_number, pin, balance) VALUES (?, ?, ?, ?, ?, ?)", 
                       (account_number, user_id, full_name, phone_number, pin, balance))
        connection.commit()
        console.print("[bold green]Account successfully created and stored in DB[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error in account insertion: {e}[/bold red]")
    finally:
        connection.close()

def get_user_id_of_user_from_db(username, password):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        
        if result:
            user_id = result[0]
            return user_id
        else:
            return None
    except Exception as e:
        console.print(f"[bold red]An error occurred in getting the user_id: {e}[/bold red]")
        return None
    finally:
        connection.close()

def get_user_accounts(username, password):
    user_id_of_user = get_user_id_of_user_from_db(username, password)
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id_of_user,))
        account = cursor.fetchone()
        if account:
            account_number = account[0]
            return account_number
        else:
            return None
    except Exception as e:
        console.print(f"[bold red]Error in getting the account number of the user: {e}[/bold red]")
    finally:
        connection.close()

def get_account_details(account_number, pin):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM accounts WHERE account_number = ? AND pin = ?", (account_number, pin))
    account = cursor.fetchone()

    try:
        if account:
            account_details = {
                "account_number": account[0],
                "full_name": account[2],
                "phone_number": account[3],
                "balance": account[5]
            }
            return account_details
        else:
            console.print("[bold red]Account not found[/bold red]")
            return None
    except Exception as e:
        console.print(f"[bold red]Error in getting account details: {e}[/bold red]")
        return None
    finally:
        connection.close()

def get_update_account_balance(account_num, new_balance, pin):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ? AND pin = ?", (new_balance, account_num, pin))
        connection.commit()
        console.print("[bold green]Balance updated successfully[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error in updating the balance in DB: {e}[/bold red]")
    finally:
        connection.close()

def get_account_owner_id(account_number, pin):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT user_id FROM accounts WHERE account_number = ? AND pin = ?", (account_number, pin))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            console.print("[bold red]Account not found[/bold red]")
            return None
    except Exception as e:
        console.print(f"[bold red]Error in getting account owner ID: {e}[/bold red]")
        return None
    finally:
        connection.close()

# Function to check username and password
def check_user_in_db(username, password):
    from Menu import login_menu  # login_menu function import
    from Auth import login       # login function import
    
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            stored_username = user[1]
            stored_password = user[2]
            if password == stored_password and username == stored_username:
                console.print("[bold green]\n********** Login successful **********\n[/bold green]") 
                login_menu(stored_username)
            elif username == stored_username and password != stored_password:
                console.print("[bold red]Wrong password[/bold red]")
                login()
            else:
                console.print("[bold red]Login failed[/bold red]")
                login()
        else:
            console.print("[bold red]User not found ** PLEASE REGISTER **[/bold red]")
    except sqlite3.Error as e:
        console.print(f"[bold red]An error occurred while checking data: {e}[/bold red]")
        return None
    finally:
        connection.close()

# Creating database and tables
create_db_and_tables()
