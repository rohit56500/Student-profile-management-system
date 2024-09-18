import loginpage
import admindashboard
import studentdashboard

def main():
    print("Welcome to the Student Profile System!")
    while True:
        role = loginpage.Login.login_display()

        if role == 'admin':
            admindashboard.AdminFunction.display_admin_dashboard()
        elif role == 'teacher':
            # Add code to display teacher dashboard
            pass
        elif role == 'student':
            studentdashboard.StudentDashboard.display_student_dashboard()
        else:
            print("Role not recognized or login failed.")

        exit_choice = input("Do you want to exit the program? (yes/no): ").strip().lower()
        if exit_choice == 'yes':
            print("Exiting the program. Goodbye!")
            break

