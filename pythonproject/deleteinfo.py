import pandas as pd
import fileerrorhandle

class delete_user:
    def __init__(self, id_number):
        user_file = fileerrorhandle.read_from_csv("users.csv")
        try:
            id_number = int(id_number)
            if id_number in user_file['id'].values:
                self.id_number = id_number
            else:
                raise ValueError("ID doesn't exist! Enter the correct ID.")
        except:
            print("Invalid ID number!")
        
    def delete_info(self):
        self.delete_info_user_file()
        self.delete_info_password_file()
        check_role = fileerrorhandle.read_from_csv("users.csv")
        if check_role.loc[check_role[id] == self.id_number, 'role'].values[0] == 'student':
            self.delete_info_eca_file()
            self.delete_info_grades_file()

    def delete_info_user_file(self):
        user_file = fileerrorhandle.read_from_csv("users.csv")
        if self.id_number in user_file['id'].values:
            user_file = user_file[user_file['id'] != self.id_number]
            fileerrorhandle.append_to_csv("users.csv", user_file)
            print("User info has been deleted from users file!")
        else:
            print("Error: User info couldn't be deleted from users file!")
    
    def delete_info_password_file(self):
        password_file = fileerrorhandle.read_from_csv("password.csv")
        if self.id_number in password_file['id'].values:
            password_file = password_file[password_file['id'] != self.id_number]
            fileerrorhandle.append_to_csv("password.csv", password_file)
            print("User info has been deleted from password file!")
        else:
            print("Error: User info couldn't be deleted from password file!")
    
    def delete_info_eca_file(self):
        eca_file = fileerrorhandle.read_from_csv("eca.csv")
        if self.id_number in eca_file['id'].values:
            eca_file = eca_file[eca_file['id'] != self.id_number]
            eca_file.to_csv("eca.csv", index=False)
            print("User info has been deleted from ECA file!")
        else:
            print("Error: User info couldn't be deleted from ECA file!")
    
    def delete_info_grades_file(self):
        grades_file = fileerrorhandle.read_from_csv("grades.csv")
        if self.id_number in grades_file['id'].values:
            grades_file = grades_file[grades_file['id'] != self.id_number]
            grades_file.to_csv("grades.csv", index=False)
            print("User info has been deleted from grades file!")
        else:
            print("Error: User info couldn't be deleted from grades file!")
