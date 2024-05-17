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


def insert_user_to_db(user_id, username, password, full_name, phone_number, email, date_of_birth ):
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





def check_data_from_db(username, password):
    from Menu import login_menu                         # login_menu function imported
    from Auth import login                              # login function imported
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
        user = cursor.fetchone()

        if user:
            stored_username = user[1]
            stored_password = user[2]
            if password == stored_password and username == stored_username:
                print("\n ********** \t\t\t login successful \t\t\t ********** \n") 
                login_menu(stored_username)
            elif username == stored_username and password != stored_password:
                print("wrong password ")
                login()
            else:
                print("login failed")
                login()
        else:
            print("User not found ** PLEASE REGISTER ** ") 
    except Exception as e:
        print(f"An error occured at checking data : {e}")

    finally: 
        connection.close()


def check_account_exists_in_db(user_id):
    try:
        cursor.execute("SELECT * from accounts WHERE user_key = ?",(user_id,))
        account = cursor.fetchone()

        if account:
            stored_key = account[0]
            stored_account_number = account[1]
            if stored_key == user_id and stored_account_number == '':
                return True
            else:
                print("account number already exists")
        else:
            print("not found the id in the system")            
    except Exception as e:
        print(f"database check account method {e}")
    finally:
        connection.close()            

def get_user_details_from_db(user_id):
    cursor.execute("SELECT full")