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
                user_key TEXT NOT NULL,
                account_number INTEGER PRIMARY KEY,
                balance REAL NOT NULL,
                FOREIGN KEY (user_key) REFERENCES users(user_id)
            )
                ''')


def insert_user(user_id, username, password, full_name, phone_number, email, date_of_birth ):
    try:
        cursor.execute("INSERT INTO users (user_id,username, password,full_name, phone_Number, email, date_Of_Birth) VALUES (?, ?, ?, ?, ?,?,?)",
                            (user_id, username, password, full_name, phone_number, email, date_of_birth))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f" error in inserting user:  {e}")

    finally:
        connection.close()

def fetch_data():
    cursor.execute("SELECT * FROM users")
    for rows in cursor.fetchall():
        print(rows)





def check_data(username, password):
    from Menu import login_menu                         # login_menu function imported
    from Auth import login                              # login function imported
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
        user = cursor.fetchone()

        if user:
            stored_username = user[1]
            stored_password = user[2]
            if password == stored_password and username == stored_username:
                print("login successful") 
                login_menu(stored_username)
            else:
                

                print("login failed")
                login()
        else:
            print("User not found ** PLEASE REGISTER ** ") 
    except Exception as e:
        print(f"An error occured: {e}")

    finally: 
        connection.close()


def save_balance_to_database(balance, user_key):
    cursor.execute("INSERT INTO accounts WHERE user_key = ?",(user_key,))
    user_account = cursor.fetchone()

    if user_account:
        stored_user_key = user_account[0]
        if stored_user_key == user_key:
            print("balance need to be added")
