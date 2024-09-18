import registeruser
import modifyinfo
import displayinfo
import deleteinfo
import fileerrorhandle
import visualizer

class AdminFunction:

    @staticmethod
    def admin_register_user():
        first_name = input("First name: ")
        last_name = input('Last name: ')
        email = input('Email: ')
        role = input('Role: ')
        address = input("Address: ")
        obj = registeruser.register_user(first_name, last_name, email, role, address)
        obj.register_user()

    @staticmethod
    def admin_edit_personal_info():
        id_number = input("Student's ID number: ")
        obj = modifyinfo.ModifyInfo(id_number)
        print("1. First name")
        print("2. Last name")
        print("3. Email")
        print("4. Role")
        print("5. Address")
        choice = input("What element do you want to change?")
        match choice:
            case '1':
                edit_element = 'first_name'
                edit_into = input("What would you like to edit it into?")
                obj.edit_user_info(edit_element, edit_into)
            case '2':
                edit_element = 'last_name'
                edit_into = input("What would you like to edit it into?")
                obj.edit_user_info(edit_element, edit_into)
            case '3':
                new_email = input("New Email Address: ")
                obj.edit_email(new_email)
            case '4':
                new_role = input("New role: ")
                obj.edit_role(new_role)
            case '5':
                new_address = input("New address: ")
                obj.edit_address(new_address)
            case _:
                print("Enter a valid number.")
    
    @staticmethod
    def admin_change_password():
        id_number = input("Student's ID number: ")
        obj = modifyinfo.ModifyInfo(id_number)
        new_password = input("New password: ")
        obj.change_password(new_password)

    @staticmethod
    def admin_edit_grades():
        id_number = input("Student's ID number: ")
        obj = modifyinfo.ModifyInfo(id_number)
        print("1. English")
        print("2. Maths")
        print("3. Science")
        print("4. Nepali")
        print("5. Computer Science")
        subject = input("Which subject would you like to edit the grade for?")
        new_marks = input("New grades: ")
        obj.edit_grades(subject, new_marks)

    @staticmethod
    def admin_delete_user():
        id_number = input("Student's ID number: ")
        obj = deleteinfo.delete_user(id_number)
        obj.delete_info()

    @staticmethod
    def admin_edit_eca():
        id_number = input("Student's ID number: ")
        obj = modifyinfo.ModifyInfo(id_number)
        new_eca = input("What would you like to change your ECA into?")
        obj.edit_eca(new_eca)

    @staticmethod
    def display_admin_dashboard():
        while True:
            print("\nAdmin Dashboard")
            print("1. Register user")
            print("2. Modify user information")
            print("3. Delete user")
            print("4. Display information")
            print("5. Visualization")
            print("6. Exit")
            choice = input("What would you like to do? ")

            match choice:
                case '1':
                    AdminFunction.admin_register_user()
                case '2':
                    print("1. Edit personal information")
                    print("2. Change password")
                    print("3. Edit grades")
                    print("4. Edit ECA")
                    choice = input("What would you like to do? ")
                    match choice:
                        case '1':
                            AdminFunction.admin_edit_personal_info()
                        case '2':
                            AdminFunction.admin_change_password()
                        case '3':
                            AdminFunction.admin_edit_grades()
                        case '4':
                            AdminFunction.admin_edit_eca()
                        case _:
                            print("Enter a valid number.")
                case '3':
                    AdminFunction.admin_delete_user()
                case '4':
                    print("1. Users")
                    print("2. ECA")
                    print("3. Grades")
                    choice = input("Which file would you like to see? ")
                    match choice:
                        case '1':
                            users = fileerrorhandle.read_from_csv("users.csv")
                            print(users)
                        case '2':
                            eca = fileerrorhandle.read_from_csv("eca.csv")
                            print(eca)
                        case '3':
                            grades = fileerrorhandle.read_from_csv("grades.csv")
                            print(grades)
                        case _:
                            print("Enter a valid number.")
                case '5':
                    print("1. ECA pie chart")
                    print("2. Average grades across subjects")
                    print("3. Grade distribution")
                    print("4. Radar chart")
                    print("5. Average marks of all students")
                    choice = input("Which visualization would you like to see?")
                    match choice:
                        case '1':
                            visualizer.eca_pie_chart()
                        case '2':
                            visualizer.average_grades_across_subjects()
                        case '3':
                            visualizer.distribution_of_grades()
                        case '4':
                            visualizer.radar_chart()
                        case '5':
                            visualizer.average_all()
                case '6':
                    print("Exiting Admin Dashboard.")
                    break
                case _:
                    print("Enter a valid number.")



