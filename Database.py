import sqlite3

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
            Pin INTEGER NOT NULL, 
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
    except Exception as e:
        print(f"Error in inserting user: {e}")
    finally:
        connection.close()

# Function to insert account into database
def insert_acc_into_db(account_number, full_name, phone_number, Pin, balance):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO accounts (account_number, full_name, phone_number, Pin, balance) VALUES (?, ?, ?, ?, ?)", 
                       (account_number, full_name, phone_number, Pin, balance))
        print("Account successfully created and stored in DB")
        connection.commit()
    except Exception as e:
        print(f"Error in account insertion: {e}")
    finally:
        connection.close()


def get_account_details(account_number):

    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
    account = cursor.fetchone()

    try:
        if account:
            account_details = {
                "account_number " : account[0],
                "full_name" : account[1],
                "phone_number" :account[2],
                "balance" : account[3]
            }
            return account_details
        else:
            print("account not found")
            return None
    except Exception as e:
        print(f"Error in getting account details: {e}")
        return None
    finally:
        connection.close()  

def get_update_account_balance(account_num, new_balance):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_num,))
        connection.commit()
        print("Balance updated successfully")
    except Exception as e:
        print(f"Error in updating the balance in db: {e}")
    finally:
        connection.close()


def get_account_owner_id(account_number):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT user_id FROM accounts WHERE account_number = ?", (account_number,))
        result = cursor.fetchone()
        if result:
            return result[0]  # Return the user_id if account is found
        else:
            print("Account not found")
            return None
    except Exception as e:
        print(f"Error in getting account owner ID: {e}")
        return None
    finally:
        connection.close()

# Function to check username and password
def check_data_from_db(username, password):
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
                print("\n ********** \t\t\t Login successful \t\t\t ********** \n") 
                login_menu(stored_username)
            elif username == stored_username and password != stored_password:
                print("Wrong password")
                login()
            else:
                print("Login failed")
                login()
        else:
            print("User not found ** PLEASE REGISTER **")
    except Exception as e:
        print(f"An error occurred while checking data: {e}")
    finally:
        connection.close()

# Creating database and tables
create_db_and_tables()
