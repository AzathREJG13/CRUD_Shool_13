# Dates_Teachers = [fist_name, last_name, shool_branch]
# Teachers = {id_teachers: Dates_Teachers}
import random

class Teacher:
    def __init__(self):
        self.id_teachers = None
        self.name = None
        self.last_name = None
        self.schol_branch = None
        self.dates_teachers = []
        self.teachers = {}
        self.assigned_ids = set()

    def list_dates_teachers(self):
        dates = [self.name, self.last_name, self.schol_branch]
        self.dates_teachers.append(dates)
        self.teachers[self.id_teachers] = dates
        print(self.teachers)

    def view_dates_teachers(self):
        if self.teachers:
            print(self.teachers)
        else:
            print("No teachers have been added yet.")

    def login_teachers(self):
        while True:
            new_id = random.randint(1, 1000)
            if new_id not in self.assigned_ids:
                self.id_teachers = new_id
                self.assigned_ids.add(new_id)
                break
            else:
                print(f"ID {new_id} already assigned. Generating a new one.")
        self.name = input('First Name teacher: ').lower()
        self.last_name = input('Last name teacher: ').lower()
        self.schol_branch = self.select_branch()
        print(f"Teacher ID generated: {self.id_teachers}")

    def select_branch(self):
        while True:
            branch = input('Enter M (Math), P (Physics), L (Language), C (Chemistry): ').lower()
            if branch == 'm':
                return 'math'
            elif branch == 'p':
                return 'physics'
            elif branch == 'l':
                return 'language'
            elif branch == 'c':
                return 'chemistry'
            else:
                print('Error: Invalid input. Please try again.')

    def update_teachers(self):
        search_id = int(input('ID: '))
        search = self.teachers.get(search_id)
        if search is None:
            print('No teacher found with that ID.')
            return
        update_list = list(search)
        print(update_list)
        while True:
            update = input('Update First Name(N), Last Name(L), Branch(B): ').lower()
            if update == 'n':
                update_list[0] = input('New First Name: ').lower()
                self.teachers[search_id] = update_list
                print(f"Updated: {self.teachers[search_id]}")
                break
            elif update == 'l':
                update_list[1] = input('New Last Name: ').lower()
                self.teachers[search_id] = update_list
                print(f"Updated: {self.teachers[search_id]}")
                break
            elif update == 'b':
                update_list[2] = self.select_branch()  
                self.teachers[search_id] = update_list
                print(f"Updated: {self.teachers[search_id]}")
                break
            else:
                print('Error: Invalid option.')

    def eliminate_teachers(self):
        search_eliminate = int(input('ID teachers: '))
        if self.teachers.get(search_eliminate) is None:
            print('No teachers found with that ID.')
            return
        del self.teachers[search_eliminate]
        print(f'Teacher with ID {search_eliminate} has been eliminated.')
        print(self.teachers)

school_teachers = Teacher()

while True:
    opcion = input('L - login teacher, V - view teachers, U - update, D - delete teacher, X - exit: ').lower()
    if opcion == 'l':
        school_teachers.login_teachers()
        school_teachers.list_dates_teachers()
    elif opcion == 'v':
        school_teachers.view_dates_teachers()
    elif opcion == 'x':
        print('Exit')
        break
    elif opcion == 'u':
        school_teachers.update_teachers()
    elif opcion == 'd':
        school_teachers.eliminate_teachers()
    else:
        print('Error: invalid option')
