import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def eca_pie_chart():
    file_path = 'eca.csv'#change file path

    data = pd.read_csv(file_path)

    # Count the occurrences of each extra-curricular activity
    activity_counts = data['eca'].value_counts()

    # Plot the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Extra-Curricular Activities')
    plt.show()

def average_grades_across_subjects():
    # Load the CSV file
    file_path = 'grades.csv'
    grades_df = pd.read_csv(file_path)

    # Calculate the average grades for each subject
    average_grades = grades_df[['english', 'maths', 'science', 'nepali', 'computer science']].mean()

    # Create a bar chart to compare the average grades of students across different subjects
    plt.figure(figsize=(10, 6))
    average_grades.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.title('Average Grades Across Subjects')
    plt.xlabel('Subjects')
    plt.ylabel('Average Grades')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)  # assuming grades are out of 100
    plt.grid(axis='y')

    # Show the plot
    plt.show()

def distribution_of_grades():
    # Load the CSV file
    file_path = 'grades.csv'
    grades_df = pd.read_csv(file_path)

    # List of subjects
    subjects = ['english', 'maths', 'science', 'nepali', 'computer science']

    # Create histograms for the distribution of grades in each subject
    plt.figure(figsize=(20, 15))

    for i, subject in enumerate(subjects, 1):
        plt.subplot(3, 2, i)
        counts, bins, patches = plt.hist(grades_df[subject], bins=range(0, 101, 2), color='skyblue', edgecolor='black')
        counts = counts.astype(int)  # Convert counts to integers
        for count, patch in zip(counts, patches):
            plt.text(patch.get_x() + patch.get_width() / 2, count, str(count), ha='center', va='bottom')
        plt.title(f'Distribution of Grades in {subject.capitalize()}')
        plt.xlabel('Grades')
        plt.ylabel('Frequency')
        plt.grid(axis='y')

    plt.tight_layout()
    plt.show()

def radar_chart():
    # Load the CSV file
    file_path = 'grades.csv'
    grades_df = pd.read_csv(file_path)

    # Select a few students for the radar chart example
    selected_students = grades_df.head(5)  # selecting the first 5 students for the example
    subjects = ['english', 'maths', 'science', 'nepali', 'computer science']

    # Function to create radar chart for a single student
    def create_radar_chart(student_data, student_name):
        # Number of variables we're plotting
        num_vars = len(subjects)

        # Compute angle of each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
        # The plot is made in a circular (not polygon) space, so we need to "complete the loop"
        student_data += student_data[:1]
        angles += angles[:1]
    
        # Create the radar chart
        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    
        ax.fill(angles, student_data, color='skyblue', alpha=0.4)
        ax.plot(angles, student_data, color='deepskyblue', linewidth=2)

        # Fix the axis to go in the right order and start at 12 o'clock
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
    
        # Draw one axe per variable and add labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(subjects, fontsize=12, color='black')
    
        # Draw ylabels
        ax.set_rlabel_position(30)
        ax.yaxis.set_tick_params(labelsize=10)
        ax.yaxis.set_tick_params(labelcolor='grey')
        ax.yaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)
        ax.xaxis.grid(True, color='grey', linestyle='--', linewidth=0.5)
    
        # Add a title
        plt.title(student_name, size=20, color='black', y=1.1)
    
        plt.show()

        # Create radar charts for selected students
    for _, row in selected_students.iterrows():
        student_name = f"{row['first_name']} {row['last_name']}"
        student_data = row[subjects].tolist()
        create_radar_chart(student_data, student_name)

def average_all():

    # Load the CSV file
    file_path = 'grades.csv'
    grades_df = pd.read_csv(file_path)

    # Calculate the average marks for each student
    grades_df['average'] = grades_df[['english', 'maths', 'science', 'nepali', 'computer science']].mean(axis=1)

    # Create a bar chart for each student's average marks
    plt.figure(figsize=(12, 6))
    plt.bar(grades_df['first_name'] + ' ' + grades_df['last_name'], grades_df['average'], color='skyblue', edgecolor='black')
    plt.title('Average Marks of Each Student')
    plt.xlabel('Students')
    plt.ylabel('Average Marks')
    plt.xticks(rotation=90)
    plt.ylim(0, 100)  # assuming grades are out of 100
    plt.grid(axis='y')

# Show the plot
    plt.tight_layout()
    plt.show()