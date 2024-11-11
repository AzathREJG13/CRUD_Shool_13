import tkinter as tk
from tkinter import messagebox
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
    
    def update_grade(self, student_id, subject_id, new_grade):
        try:
            self.cursor.execute(
                'UPDATE Grades SET Grades = %s WHERE id_Student = %s AND id_Subjects = %s',
                (new_grade, student_id, subject_id)
            )

            if self.cursor.rowcount == 0:
                messagebox.showerror("Error", f"No grade found for student ID {student_id} in subject ID {subject_id}.")
            else:
                messagebox.showinfo("Success", "Grade updated successfully.")
                conexion.commit()  # Confirm changes

        except ValueError:
            messagebox.showerror("Error", 'Please enter valid numbers for student ID, subject ID, or grade.')

    def view_grades(self, student_id):
        try:
            self.cursor.execute('SELECT id_Subjects, Grades FROM Grades WHERE Id_student = %s', (student_id,))
            results = self.cursor.fetchall()
            
            if not results:
                messagebox.showerror("Error", f"Student with ID {student_id} has no records in the Grades table.")
            else:
                grades_text = f"Grades for student ID {student_id}:\n"
                for row in results:
                    id_subject = row[0]
                    grade = row[1]
                    grades_text += f"Subject ID: {id_subject}, Grade: {grade}\n"
                messagebox.showinfo("Grades", grades_text)
        
        except ValueError:
            messagebox.showerror("Error", 'Please enter a valid student ID.')

    def enter_grade_for_year(self, student_id):
        try:
            search = my_student.students.get(student_id)
            if search is None:
                messagebox.showerror("Error", 'No student found with this ID.')
                return
            list_search = list(search)
            year_student = list_search[2:3]

            if year_student == [1]:
                subject_range = range(101, 105)
            elif year_student == [2]:
                subject_range = range(201, 205)
            elif year_student == [3]:
                subject_range = range(301, 305)
            else:
                messagebox.showerror("Error", "Invalid year.")
                return
            
            self.keys_subjects.clear()
            self.list_subject.clear()

            self.grade_entries = {}  
            for i in subject_range:
                self.keys_subjects.append(i)
                search_subject = my_subject.subject.get(i)
                self.list_subject.append(search_subject)

            grade_window = tk.Toplevel()
            grade_window.title(f"Enter Grades for Student {student_id}")

            tk.Label(grade_window, text="Enter Grades:").grid(row=0, column=0, padx=5, pady=5)
            row = 1  

            for subject in self.list_subject:
                subject_name = str(subject[0])  
                tk.Label(grade_window, text=f"{subject_name}:").grid(row=row, column=0, padx=5, pady=5)
                entry = tk.Entry(grade_window)
                entry.grid(row=row, column=1, padx=5, pady=5)
                self.grade_entries[subject_name] = entry 
                row += 1

            def save_grades():
                try:
                    for i, subject in zip(self.keys_subjects, self.list_subject):
                        subject_name = str(subject[0])  
                        grade = float(self.grade_entries[subject_name].get())
                        self.grades_subject.append(grade)
                    
                    for i, subject in zip(self.keys_subjects, self.list_subject):
                        subject_name = str(subject[0])  
                        grade = self.grades_subject[self.keys_subjects.index(i)]
                        query = 'INSERT INTO Grades (Id_student, id_Subjects, Grades) VALUES (%s, %s, %s)'
                        datos = (student_id, i, grade)
                        cursor.execute(query, datos)  
                    conexion.commit()  

                    # Mostrar mensaje de éxito
                    messagebox.showinfo("Success", "Grades saved successfully.")
                    grade_window.destroy()  
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while saving the grades: {e}")

            # Botón de guardar
            tk.Button(grade_window, text="Save Grades", command=save_grades).grid(row=row, column=0, columnspan=2, pady=10)
        
        except ValueError:
            messagebox.showerror("Error", 'Invalid input.')

    def delete_grade(self, student_id, subject_id):
        try:
            self.cursor.execute(
                'DELETE FROM Grades WHERE id_Student = %s AND id_Subjects = %s',
                (student_id, subject_id)
            )

            if self.cursor.rowcount == 0:
                messagebox.showerror("Error", f"No grade found for student ID {student_id} in subject ID {subject_id}.")
            else:
                messagebox.showinfo("Success", f"Grade for subject ID {subject_id} for student ID {student_id} deleted successfully.")
                conexion.commit()

        except ValueError:
            messagebox.showerror("Error", 'Please enter valid numbers for student ID and subject ID.')

my_grades = Grades()

def login_grades():
    clear_entries()

    tk.Label(window, text="Student ID:").grid(row=1, column=0, padx=5, pady=5)
    entry_student_id.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(window, text="Submit", command=submit_login).grid(row=2, column=0, columnspan=2, pady=5)

def submit_login():
    try:
        student_id = int(entry_student_id.get())
        my_grades.enter_grade_for_year(student_id)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Student ID.")

def view_grades():
    clear_entries()

    tk.Label(window, text="Student ID:").grid(row=1, column=0, padx=5, pady=5)
    entry_student_id.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(window, text="Submit", command=submit_view).grid(row=2, column=0, columnspan=2, pady=5)

def submit_view():
    try:
        student_id = int(entry_student_id.get())
        my_grades.view_grades(student_id)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid Student ID.")

def update_grades():
    clear_entries()

    tk.Label(window, text="Student ID:").grid(row=1, column=0, padx=5, pady=5)
    entry_student_id.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Subject ID:").grid(row=2, column=0, padx=5, pady=5)
    entry_subject_id.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(window, text="Grade:").grid(row=3, column=0, padx=5, pady=5)
    entry_grade.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(window, text="Submit", command=submit_update).grid(row=4, column=0, columnspan=2, pady=5)

def submit_update():
    try:
        student_id = int(entry_student_id.get())
        subject_id = int(entry_subject_id.get())
        new_grade = float(entry_grade.get())
        my_grades.update_grade(student_id, subject_id, new_grade)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid information.")

def delete_grades():
    clear_entries()

    # Mostrar campos para el Student ID y Subject ID
    tk.Label(window, text="Student ID:").grid(row=1, column=0, padx=5, pady=5)
    entry_student_id.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(window, text="Subject ID:").grid(row=2, column=0, padx=5, pady=5)
    entry_subject_id.grid(row=2, column=1, padx=5, pady=5)

    # Botón de acción
    tk.Button(window, text="Submit", command=submit_delete).grid(row=3, column=0, columnspan=2, pady=5)

def submit_delete():
    try:
        student_id = int(entry_student_id.get())
        subject_id = int(entry_subject_id.get())
        my_grades.delete_grade(student_id, subject_id)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid information.")

def clear_entries():
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) > 0:  # Limpiar solo las filas donde están los campos de entrada
            widget.grid_forget()

window = tk.Tk()
window.title("Grade Management System")

menu_frame = tk.Frame(window)
menu_frame.grid(row=0, column=0, columnspan=2)

tk.Button(menu_frame, text="L - Login Grades", command=login_grades).grid(row=0, column=0, padx=5, pady=5)
tk.Button(menu_frame, text="V - View Grades", command=view_grades).grid(row=0, column=1, padx=5, pady=5)
tk.Button(menu_frame, text="U - Update Grades", command=update_grades).grid(row=1, column=0, padx=5, pady=5)
tk.Button(menu_frame, text="D - Delete Grades", command=delete_grades).grid(row=1, column=1, padx=5, pady=5)
tk.Button(menu_frame, text="X - Exit", command=window.quit).grid(row=2, column=0, columnspan=2, pady=5)

entry_student_id = tk.Entry(window)
entry_subject_id = tk.Entry(window)
entry_grade = tk.Entry(window)

def on_close():
    cursor.close()
    conexion.close()
    window.quit()

window.protocol("WM_DELETE_WINDOW", on_close)

# Iniciar la interfaz
window.mainloop()
