import pandas as pd
import fileerrorhandle

# Class for modifying user information
class ModifyInfo:
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

    #edits user info
    def edit_user_info(self, edit_element, edit_into):
        users_df = fileerrorhandle.read_from_csv("users.csv")
        if edit_element not in users_df.columns:
            print(f"Error: {edit_element} is not a valid column in users file.")
            return

        users_df.loc[users_df['id'] == self.id_number, edit_element] = edit_into
        fileerrorhandle.append_to_csv("users.csv", users_df)

        # Verifying changes
        self.verify_update(users_df, "users.csv", edit_element, edit_into)

        # Update related files if role is 'student'
        if edit_element == "first_name" or edit_element == "last_name":
            self.update_related_files(edit_element, edit_into)

    # Update related files (eca and grades) for students
    def update_related_files(self, edit_element, edit_into):
        users_df = fileerrorhandle.read_from_csv("users.csv")
        role = users_df.loc[users_df['id'] == self.id_number, 'role'].values[0]

        if role == 'student':
            # Update first name in eca file
            eca_df = fileerrorhandle.read_from_csv("eca.csv")
            eca_df.loc[eca_df['id'] == self.id_number, edit_element] = edit_into
            fileerrorhandle.append_to_csv("eca.csv", eca_df)

            # Update first name in grades file
            grades_df = fileerrorhandle.read_from_csv("grades.csv")
            grades_df.loc[grades_df['id'] == self.id_number, edit_element] = edit_into
            fileerrorhandle.append_to_csv("grades.csv", grades_df)

            # Verifying changes
            self.verify_update(eca_df, "eca", edit_element, edit_into)
            self.verify_update(grades_df, "grades", edit_element, edit_into)

    # Verifies updates in related files
    def verify_update(self, df, file_name, edit_element, edit_into):
        if df.loc[df['id'] == self.id_number, edit_element].values[0] == edit_into:
            print(f"{edit_element.capitalize()} edited successfully in {file_name} file!")
        else:
            print(f"Error: {edit_element.capitalize()} couldn't be edited in {file_name} file.")

    # Edits email
    def edit_email(self, new_email):
        self.edit_user_info("email", new_email)

    # Edits role
    def edit_role(self, new_role):
        self.edit_user_info("role", new_role)

    # Edits address
    def edit_address(self, new_address):
        self.edit_user_info("address", new_address)

    # Makes edits in password.csv
    def change_password(self, new_password):
        password_df = fileerrorhandle.read_from_csv("password.csv")
        password_df.loc[password_df['id'] == self.id_number, 'password'] = new_password
        fileerrorhandle.append_to_csv("password.csv", password_df)

        # Verifying changes
        if password_df.loc[password_df['id'] == self.id_number, 'password'].values[0] == new_password:
            print("Password changed successfully!")
        else:
            print("Error: Password couldn't be changed.")

    # Makes edits in grades.csv
    def edit_grades(self, subject, new_marks):
        grades_df = fileerrorhandle.read_from_csv("grades.csv")
        grades_df.loc[grades_df['id'] == self.id_number, subject] = new_marks
        fileerrorhandle.append_to_csv("grades.csv", grades_df)

        # Verifying changes
        if grades_df.loc[grades_df['id'] == self.id_number, subject].values[0] == new_marks:
            print("Marks edited successfully!")
        else:
            print("Error: Marks couldn't be edited.")

    # Makes edits in eca.csv
    def edit_eca(self, new_eca):
        eca_df = fileerrorhandle.read_from_csv("eca.csv")
        eca_df.loc[eca_df['id'] == self.id_number, 'eca'] = new_eca
        fileerrorhandle.append_to_csv("eca.csv", eca_df)

        # Verifying changes
        if eca_df.loc[eca_df['id'] == self.id_number, 'eca'].values[0] == new_eca:
            print("ECA changed successfully!")
        else:
            print("Error: ECA couldn't be changed.")
