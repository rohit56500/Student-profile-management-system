import modifyinfo
import displayinfo
import fileerrorhandle
import visualizer

class StudentDashboard:
    @staticmethod
    def student_edit_info():
        id_number = input("Student's ID number: ")
        obj = modifyinfo.ModifyInfo(id_number)
        print("1. First name")
        print("2. Last name")
        print("3. Email")
        print("4. Role")
        print("5. Address")
        choice = input("What element do you want to change? ")
        match choice:
            case '1':
                edit_element = 'first_name'
                edit_into = input("What would you like to edit it into? ")
                obj.edit_user_info(edit_element, edit_into)
            case '2':
                edit_element = 'last_name'
                edit_into = input("What would you like to edit it into? ")
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
    def student_see_grades():
        id_number = input("Student's ID number: ")
        obj = displayinfo.display_info(id_number)
        obj.display_grades()

    @staticmethod
    def student_see_eca():
        id_number = input("Student's ID number: ")
        obj = displayinfo.display_info(id_number)
        obj.display_eca()

    @staticmethod
    def display_student_dashboard():
        while True:
            print("\nStudent Dashboard")
            print("1. Change user information")
            print("2. See grades")
            print("3. See ECA")
            print("4. See visualization")
            print("5. Exit")
            choice = input("What would you like to do today? ")

            match choice:
                case '1':
                    StudentDashboard.student_edit_info()
                case '2':
                    StudentDashboard.student_see_grades()
                case '3':
                    StudentDashboard.student_see_eca()
                case '4':
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
                case '5':
                    print("Exiting Student Dashboard.")
                    break
                case _:
                    print("Enter a valid number.")


