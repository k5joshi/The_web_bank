import sqlite3
from Menu import login_menu

connection = sqlite3.connect("Users_data.db")
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users_data(
                user_id TEXT PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                full_Name TEXT NOT NULL,
                phone_Number TEXT NOT NULL,
                email TEXT NOT NULL,
                date_Of_Birth DATE NOT NULL
                )

''')

def insert_user(user_id, username, password, full_name, phone_number, email, date_of_birth ):
    try:
        cursor.execute("INSERT INTO Users_data (user_id, username, password,full_name, phone_Number, email, date_Of_Birth) VALUES (?, ?, ?, ?, ?,?,?)",
                            (user_id, username, password, full_name, phone_number, email, date_of_birth))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(f" error in inserting user:  {e}")

def fetch_data():
    cursor.execute("SELECT * FROM Users_data")
    for rows in cursor.fetchall():
        print(rows)


def check_data(username, password):
    try:
        from Auth import login
        cursor.execute("SELECT * FROM Users_data WHERE username = ?",(username,))
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
