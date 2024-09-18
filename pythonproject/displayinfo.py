import pandas as pd
import fileerrorhandle

class display_info():
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
        
    def display_user_info(self):
        user_file = fileerrorhandle.read_from_csv("users.csv")
        user_row = user_file[user_file['id'] == self.id_number]
        print(user_row)

    def display_grades(self):
        grades_file = fileerrorhandle.read_from_csv("grades.csv")
        grades_row = grades_file[grades_file['id'] == self.id_number]
        print(grades_row)

    def display_eca(self):
        eca_file = fileerrorhandle.read_from_csv("eca.csv")
        eca_row = eca_file[eca_file['id'] == self.id_number]
        print(eca_row)
       