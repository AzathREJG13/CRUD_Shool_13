from mysql_conexion import cursor, conexion

import random

class Teachers:
    def __init__(self):
        self.id_teacher = None
        self.name = None
        self.last_name = None
        self.branch = None
        self.dates_teacher = []
        self.teachers = {}
        self.assigned_ids = set()

    def builder(self):
        consulta = 'SELECT * FROM Teachers'
        cursor.execute(consulta)
        result = cursor.fetchall()
        for i in result:
            id_teacher = i[0]
            dates_sql = [i[1], i[2], i[3]]
            self.teachers[id_teacher] = dates_sql
            self.assigned_ids.add(id_teacher)

    def list_dates_teacher(self):
        dates = [self.name, self.last_name, self.branch]
        self.dates_teacher.append(dates)
        self.teachers[self.id_teacher] = dates
        print(self.teachers)
        consulta = 'INSERT INTO Teachers (id_Teachers, First_Name, Last_Name, Branch) VALUES (%s, %s, %s, %s)'
        cursor.execute(consulta, (self.id_teacher, *dates))
        conexion.commit()
        print('Teacher data inserted into database.')

    def view_dates_teachers(self):
        if self.teachers:
            print(self.teachers)
        else:
            print("No teachers have been added yet.")
    
    def login_teachers(self):
        while True:
            new_id = random.randint(1000, 2000)
            if new_id not in self.assigned_ids:
                self.id_teacher = new_id
                self.assigned_ids.add(new_id)
                break
            else:
                print(f"ID {new_id} already assigned. Generating a new one.")
        self.name = input('First Name of teacher: ').lower()
        self.last_name = input('Last Name of teacher: ').lower()
        while True:
            area = input("Enter the branch (C for Chemistry, M for Math, P for Physics, L for Language): ").lower()
            if area == 'c':
                self.branch = 'chemistry'
                break
            elif area == 'm':
                self.branch = 'math'
                break
            elif area == 'p':
                self.branch = 'physics'
                break
            elif area == 'l':
                self.branch = 'language'
                break
            else:
                print('Invalid branch. Please enter C, M, P, or L.')
        print(f"Teacher ID generated: {self.id_teacher}")

    def update_teachers(self):
        search_id = int(input('ID of teacher: '))
        search = self.teachers.get(search_id)
        if search is None:
            print('No teacher found.')
            return
        update_list = list(search)
        print(update_list)
        while True:
            update = input('Update First Name(N), Last Name(L), Branch(B): ').lower()
            if update == 'n':
                update_list.pop(0)
                new_name = input('First Name: ').lower()
                update_list.insert(0, new_name)
                print(update_list)
                self.teachers[search_id] = update_list
                print(self.teachers)
                consulta_update = 'UPDATE Teachers SET First_Name = %s WHERE id_Teachers = %s'
                cursor.execute(consulta_update, (new_name, search_id))
                conexion.commit()
                print("Teacher data updated.")
                break
            elif update == 'l':
                update_list.pop(1)
                new_last_name = input('Last Name: ').lower()
                update_list.insert(1, new_last_name)
                print(update_list)
                self.teachers[search_id] = update_list
                print(self.teachers)
                consulta_update = 'UPDATE Teachers SET Last_Name = %s WHERE id_Teachers = %s'
                cursor.execute(consulta_update, (new_last_name, search_id))
                conexion.commit()
                print("Teacher data updated.")
                break
            elif update == 'b':
                while True:
                    update_list.pop(2)
                    area_2 = input("Enter the branch (C for Chemistry, M for Math, P for Physics, L for Language): ").lower()
                    if area_2 == 'c':
                        new_branch = 'chemistry'
                        break
                    elif area_2 == 'm':
                        new_branch = 'math'
                        break
                    elif area_2 == 'p':
                        new_branch = 'physics'
                        break
                    elif area_2 == 'l':
                        new_branch = 'language'
                        break
                    else:
                        print('Invalid branch. Please enter C, M, P, or L.')
                update_list.insert(2, new_branch)
                print(update_list)
                self.teachers[search_id] = update_list
                print(self.teachers)
                consulta_update = 'UPDATE Teachers SET Branch = %s WHERE id_Teachers = %s'
                cursor.execute(consulta_update, (new_branch, search_id))
                conexion.commit()
                print("Teacher data updated.")
                break
            else:
                print('Error.')

    def eliminate_teacher(self):
        search_eliminate = int(input('ID of teacher: '))
        if self.teachers.get(search_eliminate) is None:
            print('No teacher found with that ID.')
            return
        del self.teachers[search_eliminate]
        print(f'Teacher with ID {search_eliminate} has been eliminated.')
        print(self.teachers)
        consulta_delete = 'DELETE FROM Teachers WHERE id_Teachers = %s'
        cursor.execute(consulta_delete, (search_eliminate,))
        conexion.commit()
        print('Teacher has been eliminated')

school_teachers = Teachers()
if __name__ == "__main__":
    while True:
        opcion = input('L - login teacher, V - view teachers, U - update, D - delete teacher, X - exit: ').lower()
        if opcion == 'l':
            school_teachers.login_teachers()
            school_teachers.list_dates_teacher()
        elif opcion == 'v':
            school_teachers.builder()
            school_teachers.view_dates_teachers()
        elif opcion == 'x':
            print('Exit')
            cursor.close()
            conexion.close()
            break
        elif opcion == 'u':
            school_teachers.update_teachers()
        elif opcion == 'd':
            school_teachers.eliminate_teacher()
        else:
            print('Error: invalid option')
