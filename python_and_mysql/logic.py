import random

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
        self.name = input('Fist Name student: ').lower()
        self.last_name = input('Last name student: ').lower()
        while True:
            try:
                year_school = int(input('Year of school: '))
                if year_school <= 3 :
                    self.year_school = year_school
                    break
                else:
                    print('There are only 3 school years.')
            except ValueError: 
                print('Pls enter a valid number.')

        print(f"Student ID generated: {self.id_student}")
    
    def update_students(self):
        serch_id = int(input('ID : '))
        serch = self.students.get(serch_id)
        if serch is None:
            print('No student')
            return
        update_list = list(serch)
        print(update_list)
        while True:
            update = input('Update First Name(N), Last Name(L), Shool_year(Y):  ').lower()
            if update == 'n':
                update_list.pop(0)
                new_name = input('Fist Name: ').lower()
                update_list.insert(0, new_name)
                print(update_list)
                self.students[serch_id] = update_list
                print(self.students)
                break
            elif update == 'l':
                update_list.pop(1)
                new_last_name = input('Last Name: ').lower()
                update_list.insert(1, new_last_name)
                print(update_list)
                self.students[serch_id] = update_list
                print(self.students)
                break
            elif update == 'y':
                update_list.pop(2)
                new_year = int(input('Shool year: '))
                update_list.insert(2, new_year)
                print(update_list)
                self.students[serch_id] = update_list
                print(self.students)
                break
            else:
                print('Error.')

    def eliminate_student(self):
        search_eliminate = int(input('ID student: '))
        if self.students.get(search_eliminate) is None:
            print('No student found with that ID.')
            return
        del self.students[search_eliminate]
        print(f'Student with ID {search_eliminate} has been eliminated.')
        print(self.students)

school_students = Student()


while True:
    opcion = input('L - login student, V - view students, U - update, D - delete student, X - exit:  ').lower()
    if opcion == 'l':
        school_students.login_students()
        school_students.list_dates_student()
    elif opcion == 'v':
        school_students.view_dates_students()
    elif opcion == 'x':
        print('Exit')
        break
    elif opcion == 'u':
        school_students.update_students()
    elif opcion == 'd':
        school_students.eliminate_student()
    else:
        print('Error: invalid option')
