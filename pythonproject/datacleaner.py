import pandas as pd

user_file = pd.read_csv('users.csv')
students = user_file[user_file['role'] == 'student']
eca = students[['id', 'first_name', 'last_name']].copy()
eca['eca'] = None
grades = students[['id', 'first_name', 'last_name']].copy()
grades['english'] = None
grades['maths'] = None
grades['science'] = None
grades['nepali'] = None
grades['computer science'] = None
eca.to_csv('eca.csv', index=False)
grades.to_csv('grades.csv', index=False)
