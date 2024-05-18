import sqlite3

connection = sqlite3.connect("Database.db")
cursor= connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                full_Name TEXT NOT NULL,
                phone_Number TEXT NOT NULL,
                email TEXT NOT NULL,
                date_Of_Birth [DATE] NOT NULL
                )

                ''')
cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts(
                account_number INTEGER PRIMARY KEY,
                full_name TEXT NOT NULL,
                phone_number INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )
                ''')




# function to insert the created user into the database 

def insert_user_to_db(user_id, username, password, full_name, phone_number, email, date_of_birth ):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (user_id,username, password,full_name, phone_Number, email, date_Of_Birth) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (user_id, username, password, full_name, phone_number, email, date_of_birth,))
        connection.commit()
    except Exception as e:
        print(f" error in inserting user:  {e}")


def insert_acc_into_db(account_number, full_name, phone_number, balance):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO accounts (account_number,full_name, phone_number,balance) VALUES (?, ?, ?, ?)",               (account_number, full_name, phone_number, balance,))
        connection.commit()

        print("account successfully created and stored in db")
    except Exception as e:
        print(f"error in account insertion : {e}")

    connection.close()

def insert_only_balance_in_account(account_number, amount):
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM accounts WHERE account_number =?",(account_number))
        account = cursor.fetchone()

        if account:
            stored_account_num =  account[0]
           
            if stored_account_num == account_number:
                account[3] = amount                 
                return True
            
        else:
            print("amount is saved successfully")
    except Exception as e:
        print(f"error in insert_balance_only: {e}")
    
    connection.close()