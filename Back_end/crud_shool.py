import random
import mysql.connector 

class Student:
    def __init__(self):
        self.id_student = None
        self.name = None
        self.last_name = None
        self.year_school = None
        self.dates_students = []
        self.students = {}
    
    def list_dates_student(self):
        dates = [self.name, self.last_name, self.year_school]
        self.dates_students.append(dates)        
        self.students[self.id_student] = dates
        print(self.students)
    
    def view_dates_students(self):
        if self.students:
            print(self.students)
        else:
            print("No students have been added yet.")
    
    def login_students(self):
        self.id_student = random.randint(1, 1000)  
        self.name = input('Name student: ').lower()
        self.last_name = input('Last name student: ').lower()
        self.year_school = input('Year of school: ')
        print(f"Student ID generated: {self.id_student}")

school_students = Student()

while True:
    opcion = input('L - login student, V - view students, X - exit:  ').lower()
    if opcion == 'l':
        school_students.login_students()
        school_students.list_dates_student()
    elif opcion == 'v':
        school_students.view_dates_students()
    elif opcion == 'x':
        print('Exit')
        break
    else:
        print('Error: invalid option')
