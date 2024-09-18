import pandas as pd
import fileerrorhandle

class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password

    @staticmethod
    def login_display():
        id = input("Enter your user ID: ")
        password = input("Enter your password: ")
        login_obj = Login(id, password)
        return login_obj.check_login_details()

    #checks login details and role of the user
    def check_login_details(self):
        id_password = fileerrorhandle.read_from_csv("password.csv")
        try:
            self.id = int(self.id)
        except ValueError:
            print("Incorrect login credentials! Try again.")
            return None  # Return None if ID conversion fails
        
        user_record = id_password.loc[(id_password['id'] == self.id) & (id_password['password'] == self.password)]

        if not user_record.empty:
            print("Login successful!")
            role = user_record.iloc[0]['role']
            if role in ['admin', 'student', 'teacher']:  # Ensure role is valid
                return role
            else:
                print("Unknown role!")
                return None
        else:
            print("Incorrect login credentials! Try again.")
            return None

#testing
#obj = login(20240501, 'iloveshritika123')
#obj.check_login_details()
