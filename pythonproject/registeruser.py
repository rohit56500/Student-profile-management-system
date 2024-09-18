import pandas as pd
import datetime
import string
import random
import fileerrorhandle

#has methods used in registering a user
class register_user:
    def __init__(self, first_name, last_name, email, role, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.address = address
        self.id_number = self.unique_id_generator()
        self.password = self.password_generator()
    
    #registers user
    def register_user(self):
        self.update_user_file()
        self.update_password_file()
        if self.role == 'student':
            self.update_grades_file()
            self.update_eca_file()

    #generates unique id
    @staticmethod
    def unique_id_generator():
        current_year = str(datetime.datetime.now().year)
        try:
            users = pd.read_csv("users.csv")
            last_part_id = str(users.iloc[-1]['id'])[4:8]
            new_id = int(current_year + '0' + str(int(last_part_id) + 1))
        except (FileNotFoundError, pd.errors.EmptyDataError):
            new_id = int(current_year + '0001')
        return new_id
        
    
    #generates password
    @staticmethod
    def password_generator():
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        return password
    
    #registers new users into users.csv
    def update_user_file(self):     #GLOBAL BATA SELF. BANAUNE
        new_user = {'id': self.id_number, 
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'email': self.email,
                    'role': self.role,
                    'address': self.address}
        new_user_df = pd.DataFrame([new_user])
        fileerrorhandle.append_to_csv("users.csv", new_user_df)
        users = fileerrorhandle.read_from_csv("users.csv")
        if users.loc[users['id'] == self.id_number].empty:
            print("Error: User registration failed.")
        else:
            print("User registered successfully!")
            print(f"ID: {self.id_number}, Password: {self.password}")
    
    #registers new users into password.csv
    def update_password_file(self):
        new_password = {'id': self.id_number, 
                        'password': self.password, 
                        'role': self.role}
        new_password_df = pd.DataFrame([new_password])
        fileerrorhandle.append_to_csv("password.csv", new_password_df)
        password_file = fileerrorhandle.read_from_csv("password.csv")
        if password_file.loc[password_file['id'] == self.id_number].empty:
            print("Error: Password couldn't be uploaded.")
        else:
            print("Password uploaded successfully!")

    #registers new users into grades.csv
    def update_grades_file(self):
        new_user_grades = {'id': self.id_number, 
                            'first_name': self.first_name,
                            'last_name': self.last_name}
        new_user_grades_df = pd.DataFrame([new_user_grades])
        fileerrorhandle.append_to_csv("grades.csv", new_user_grades_df)
        grades_file = fileerrorhandle.read_from_csv("grades.csv")
        if grades_file.loc[grades_file['id'] == self.id_number].empty:
            print("Error: Grades file couldn't be updated.")
        else:
            print("Grades file updated successfully!")

    #registers new users into eca.csv
    def update_eca_file(self):
        new_user_eca = {'id': self.id_number, 
                        'first_name': self.first_name,
                        'last_name': self.last_name}
        new_user_eca_df = pd.DataFrame([new_user_eca])
        fileerrorhandle.append_to_csv("eca.csv", new_user_eca_df)
        eca_file = fileerrorhandle.read_from_csv("eca.csv")
        if eca_file.loc[eca_file['id'] == self.id_number].empty:
            print("Error: ECA file couldn't be updated.")
        else:
            print("ECA file updated successfully!")

