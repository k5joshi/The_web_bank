import random
import string




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
        return self.__user_id
    
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
        special_characters = "!@#$%^&*()-_=+[{]}\\|;:',<.>/?"
    
        # Randomly choose 3 characters
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        
        # Randomly choose 1 special character
        random_special_char = random.choice(special_characters)
        
        # Combine random characters and special character
        user_id = random_chars + random_special_char
        
        # If the length is less than 10, add random digits to reach length 10
        while len(user_id) < 10:
            user_id += random.choice(string.digits)
        
        # Shuffle the characters to make the order random
        user_id_list = list(user_id)
        random.shuffle(user_id_list)
        user_id = ''.join(user_id_list)
        
        return user_id
    
    # create USER CREATION
    @staticmethod
    def user_creation(username, password,full_name,phone_number, email, date_of_birth):
        
        from Database import insert_user

        new_user = User(username, password,full_name, phone_number, email, date_of_birth)
        
        insert_user(new_user.get_user_id(),new_user.get_username(),new_user.get_password(),new_user.get_full_name(), new_user.get_phone_number(), new_user.get_email(), new_user.get_date_of_birth())
        print("user created successfully \n\n\n")

        
