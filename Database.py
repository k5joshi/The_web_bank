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
    except Exception as e:
        print(f"Error in inserting user: {e}")
    finally:
        connection.close()

# Function to insert account into database
def insert_acc_into_db(account_number,user_id, full_name, phone_number, pin, balance):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO accounts (account_number, user_id, full_name, phone_number, pin, balance) VALUES (?, ?, ?, ?, ?, ?)", 
                       (account_number, user_id, full_name, phone_number, pin, balance))
        print("Account successfully created and stored in DB")
        connection.commit()
    except Exception as e:
        print("\n\n",f"Error in account insertion: {e}")
    finally:
        connection.close()

def get_user_id_of_user_from_db(username, password):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username  = ? AND password = ?", (username, password))

        result = cursor.fetchone()
        
        # Check if a user was found
        if result:
            # Extract the user_id from the result
            user_id = result[0]
            return user_id
        else:
            # Return None if no user was found
            return None
    except Exception as e:
        # Print the error message and return None in case of an error
        print(f"\nAn error occurred in getting the user_id: {e}")
        return None
    finally:
        # Close the database connection
        connection.close()

def get_user_accounts(username, password):

    user_id_of_user = get_user_id_of_user_from_db(username, password)
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute(" SELECT * FROM accounts WHERE user_id = ? ", (user_id_of_user,))

        account = cursor.fetchone()
        if account:
            account_number = account[0]
            return account_number
        else:
            return None
        
    except Exception as e:
        print(f" error in getting the account number of the user :  {e}")
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
                "account_number" : account[0],
                "full_name" : account[2],
                "phone_number" :account[3],
                "balance" : account[5]
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

def get_update_account_balance(account_num, new_balance, pin):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ? AND pin = ?", (new_balance, account_num, pin))
        connection.commit()
        print("Balance updated successfully")
    except Exception as e:
        print(f"Error in updating the balance in db: {e}")
    finally:
        connection.close()


def get_account_owner_id(account_number, pin):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT user_id FROM accounts WHERE account_number = ? AND pin = ?", (account_number,pin))
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
    except sqlite3.Error as e:
        print(f"An error occurred while checking data: {e}")
        return None
    finally:
        connection.close()

# Creating database and tables
create_db_and_tables()
