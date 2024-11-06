from mysql_conexion import cursor, conexion
from students import Student
from subjects import Subject

my_student = Student()
my_student.builder()

my_subject = Subject()
my_subject.builder()

class Grades:
    def __init__(self):
        self.grades = None
        self.list_student_grades = {}
        self.grades_student_subject = {}
        self.grades_subject = []
        self.list_subject = []
        self.keys_subjects = []
        self.cursor = cursor
    
    def update_grade(self):
        try:
            id_student = int(input('Enter student ID: '))
            id_subject = int(input('Enter subject ID: '))
            new_grade = float(input('Enter new grade: '))

            self.cursor.execute(
                'UPDATE Grades SET Grades = %s WHERE id_Student = %s AND id_Subjects = %s',
                (new_grade, id_student, id_subject)
            )

            if self.cursor.rowcount == 0:
                print(f"No grade found for student ID {id_student} in subject ID {id_subject}.")
            else:
                print("Grade updated successfully.")
                conexion.commit()  # Confirm changes

        except ValueError:
            print('Error: Please enter valid numbers for student ID, subject ID, or grade.')

    def view_grades(self):
        try:
            id_student_search = int(input('Enter student ID to view grades: '))
            
            cursor.execute('SELECT id_Subjects, Grades FROM Grades WHERE Id_student = %s', (id_student_search,))
            
            results = cursor.fetchall()
            
            if not results:
                print(f"Student with ID {id_student_search} has no records in the Grades table.")
            else:
                print(f"Grades for student ID {id_student_search}:")
                for row in results:
                    id_subject = row[0]
                    grade = row[1]
                    print(f"Subject ID: {id_subject}, Grade: {grade}")
        
        except ValueError:
            print('Error: Please enter a valid student ID.')


    def builder(self):
        print(self.list_student_grades)
        for id_student, subjects in self.list_student_grades.items():
            print(f"Processing student ID: {id_student}")  
            cursor.execute("SELECT Id_student FROM Student WHERE Id_student = %s", (id_student,))
            if cursor.fetchone() is None:
                print(f"Student with ID {id_student} does not exist in the Students table.")
                continue

            for id_subject, grade in subjects.items():
                print(f"Attempting to insert - Student: {id_student}, Subject: {id_subject}, Grade: {grade}")  
                cursor.execute("SELECT id_Subjects FROM Subjects WHERE id_Subjects = %s", (id_subject,))
                if cursor.fetchone() is None:
                    print(f"Subject with ID {id_subject} does not exist in the Subjects table.")
                    continue

                query = 'INSERT INTO Grades (Id_student, id_Subjects, Grades) VALUES (%s, %s, %s)'
                datos = (id_student, id_subject, grade)
                try:
                    cursor.execute(query, datos)
                    print(f"Data inserted: {datos}")  
                except Exception as e:
                    print(f"Error inserting data into the database: {e}")

        conexion.commit()
        print('Data inserted into the database.')
        self.grades_student_subject.clear()
        self.list_subject.clear()
        self.grades_subject.clear()
        self.keys_subjects.clear()

    def enter_grade_for_year(self):
        try:
            serch_id_student = int(input('Enter student ID: '))
            serch = my_student.students.get(serch_id_student)
            if serch is None:
                print('No student found with this ID.')
                return
            list_serch = list(serch)
            year_student = list_serch[2:3]

            if year_student == [1]:
                subject_range = range(101, 105)
            elif year_student == [2]:
                subject_range = range(201, 205)
            elif year_student == [3]:
                subject_range = range(301, 305)
            else:
                print("Invalid year.")
                return
            
            for i in subject_range:
                self.keys_subjects.append(i)
                serch_subject = my_subject.subject.get(i)
                self.list_subject.append(serch_subject)
            
            print(self.list_subject)

            for i in self.list_subject:
                enter_grade = float(input(f'Enter grade for {i}: '))
                self.grades_subject.append(enter_grade)
            
            print(self.grades_subject)

            self.grades_student_subject = dict(zip(self.keys_subjects, self.grades_subject))
            self.list_student_grades[serch_id_student] = self.grades_student_subject

            print(self.list_student_grades)

        except ValueError:
            print('Error: Invalid input.')

    def delete_grade(self):
        try:
            id_student = int(input('Enter student ID: '))
            id_subject = int(input('Enter subject ID: '))

            # Execute the delete query
            self.cursor.execute(
                'DELETE FROM Grades WHERE id_Student = %s AND id_Subjects = %s',
                (id_student, id_subject)
            )

            # Confirm changes in the database
            if self.cursor.rowcount == 0:
                print(f"No grade found for student ID {id_student} in subject ID {id_subject}.")
            else:
                print(f"Grade for subject ID {id_subject} for student ID {id_student} deleted successfully.")
                conexion.commit()  # Confirm changes

        except ValueError:
            print('Error: Please enter valid numbers for student ID and subject ID.')

my_grades = Grades()

while True:
    option = input('L - Login grades, V - View grades, U - Update grades, D - Delete grades, X - Exit:  ').lower()
    if option == 'l':
        my_grades.enter_grade_for_year()
        my_grades.builder()
    elif option == 'v':
        my_grades.view_grades()
    elif option == 'u':
        my_grades.update_grade()
    elif option == 'd':
        my_grades.delete_grade()
    elif option == 'x':
        print('Exiting...')
        cursor.close()
        conexion.close()
        break
    else:
        print('Error: Invalid option.')
