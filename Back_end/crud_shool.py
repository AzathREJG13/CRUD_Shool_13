class Student:
    def __init__(self, id_student, name, last_name, year_school):
        self.id_student = id_student
        self.name = name 
        self.last_name = last_name
        self.year_school = year_school
        self.dates_students = []
        self.students = {}
    
    def view_dates_student(self, answer):
        if answer == 'yes':
            dates = [self.name, self.last_name, self.year_school]
            print(dates)
            self.dates_students.append(dates)
            print(self.dates_students)
            
            self.students[self.id_student] = dates
            print(self.students)
        else:
            print('dates NO')


enter_id = int(input('enter id: '))
enter_name = input('enter name: ')
enter_last_name = input('enter last name: ')
years = int(input('the years school: '))
my_student = Student(enter_id, enter_name, enter_last_name, years)
answer_you = input('yes or no: ').lower()
my_student.view_dates_student(answer_you)