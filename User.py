import uuid
from Database import insert_user_to_db


class User:
    
    def __init__(self,username,password,full_name, phone_number, email, date_of_birth):
        self.__user_id = self.generate_user_id()
        self.__username =username
        self.__password = password
        self.__full_name = full_name
        self.__phone_number = phone_number
        self.__email = email
        self.__date_of_birth = date_of_birth

    #----------------------------------- getters --------------------------------------

    def get_user_id(self):
        return str(self.__user_id)
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_full_name(self):
        return self.__full_name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_email(self):
        return self.__email
    
    def get_date_of_birth(self):
        return self.__date_of_birth
    
    #----------------------------------- setters ---------------------------------------

    def set_user_id(self):
        self.__user_id = self.generate_user_id()

    def set_username(self, username):
        self.__username = username
    
    def set_password(self, password):
        self.__password = password

    def set_full_name(self, full_name):
        self.__full_name = full_name
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def set_email(self, email):
        self.__email = email
    
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    

    
    def generate_user_id(self):
        user_id = uuid.uuid4()
        return user_id
    
    
    # create USER CREATION AND ALSO SAVE IT TO THE DATABASE

    def user_creation(username,password,full_name,phone_number, email, date_of_birth):
        new_user = User(username,
                        password,
                        full_name,
                        phone_number,
                        email,
                        date_of_birth)
        print(f"user created successfully \n\n\n {new_user.generate_user_id() } please save this user id for future transaction ** don't share this with anyone ** ")
        insert_user_to_db(new_user.get_user_id(),
                    new_user.get_username(),
                    new_user.get_password(),
                    new_user.get_full_name(),
                    new_user.get_phone_number(),
                    new_user.get_email(),
                    new_user.get_date_of_birth())
        


