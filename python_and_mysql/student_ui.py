import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from mysql_conexion import cursor, conexion
import random

class Student:
    def __init__(self):
        self.id_student = None
        self.name = None
        self.last_name = None
        self.year_school = None
        self.dates_students = []
        self.students = {}
        self.assigned_ids = set()

    def builder(self):
        consulta = 'SELECT * FROM Student'
        cursor.execute(consulta)
        result = cursor.fetchall()
        for i in result:
            id_stu = i[0]
            dates_sql = [i[1], i[2], i[3]]
            self.students[id_stu] = dates_sql
            self.assigned_ids.add(id_stu)

    def list_dates_student(self):
        dates = [self.name, self.last_name, self.year_school]
        self.dates_students.append(dates)        
        self.students[self.id_student] = dates
        consulta = 'INSERT INTO Student (Id_student, Fist_Name, Last_Name, Year) VALUES (%s,%s, %s, %s)'
        cursor.execute(consulta, (self.id_student, *dates))
        conexion.commit()
        print('Dates insert Database.')

    def view_dates_students(self):
        # Limpiar la tabla antes de agregar nuevos datos
        for row in tree.get_children():
            tree.delete(row)

        if self.students:
            # Agregar los estudiantes a la tabla
            for student_id, data in self.students.items():
                tree.insert("", "end", values=(student_id, *data))
        else:
            messagebox.showinfo("No Students", "No students have been added yet.")
    
    def login_students(self):
        while True:
            new_id = random.randint(1, 1000)
            if new_id not in self.assigned_ids:
                self.id_student = new_id
                self.assigned_ids.add(new_id)  
                break
        self.name = simpledialog.askstring("First Name", 'First Name student: ').lower()
        self.last_name = simpledialog.askstring("Last Name", 'Last name student: ').lower()
        
        # Restricción de año escolar entre 1 y 3
        while True:
            try:
                year_school = int(simpledialog.askstring("Year", 'Year of school (1, 2, 3): '))
                if year_school in [1, 2, 3]:
                    self.year_school = year_school
                    break
                else:
                    messagebox.showerror('Error', 'Year must be 1, 2, or 3.')
            except ValueError: 
                messagebox.showerror('Error', 'Please enter a valid number.')

        messagebox.showinfo("Student ID", f"Student ID generated: {self.id_student}")
    
    def update_students(self):
        search_id = simpledialog.askinteger("Update Student", 'ID: ')
        serch = self.students.get(search_id)
        if serch is None:
            messagebox.showinfo('Error', 'No student found with that ID.')
            return
        
        # Mostrar ventana con botones para seleccionar qué campo actualizar
        def update_first_name():
            new_name = simpledialog.askstring('First Name', 'New First Name: ').lower()
            serch[0] = new_name
            self.students[search_id] = serch
            consulta_update = 'UPDATE Student SET Fist_Name = %s WHERE Id_student = %s'
            cursor.execute(consulta_update, (new_name, search_id))
            conexion.commit()
            messagebox.showinfo("Update", "First Name updated.")
            update_window.destroy()

        def update_last_name():
            new_last_name = simpledialog.askstring('Last Name', 'New Last Name: ').lower()
            serch[1] = new_last_name
            self.students[search_id] = serch
            consulta_update = 'UPDATE Student SET Last_Name = %s WHERE Id_student = %s'
            cursor.execute(consulta_update, (new_last_name, search_id))
            conexion.commit()
            messagebox.showinfo("Update", "Last Name updated.")
            update_window.destroy()

        def update_year():
            # Restricción de año escolar entre 1 y 3
            while True:
                try:
                    new_year = int(simpledialog.askstring('Year', 'New School Year (1, 2, 3): '))
                    if new_year in [1, 2, 3]:
                        serch[2] = new_year
                        self.students[search_id] = serch
                        consulta_update = 'UPDATE Student SET Year = %s WHERE Id_student = %s'
                        cursor.execute(consulta_update, (new_year, search_id))
                        conexion.commit()
                        messagebox.showinfo("Update", "School Year updated.")
                        update_window.destroy()
                        break
                    else:
                        messagebox.showerror('Error', 'Year must be 1, 2, or 3.')
                except ValueError: 
                    messagebox.showerror('Error', 'Please enter a valid number.')

        # Ventana para actualizar los datos
        update_window = tk.Toplevel(root)
        update_window.title("Update Student Data")

        update_button1 = tk.Button(update_window, text="Update First Name", command=update_first_name)
        update_button1.pack(pady=10)

        update_button2 = tk.Button(update_window, text="Update Last Name", command=update_last_name)
        update_button2.pack(pady=10)

        update_button3 = tk.Button(update_window, text="Update School Year", command=update_year)
        update_button3.pack(pady=10)

        cancel_button = tk.Button(update_window, text="Cancel", command=update_window.destroy)
        cancel_button.pack(pady=10)

    def eliminate_student(self):
        search_eliminate = simpledialog.askinteger('Delete Student', 'ID student: ')
        if self.students.get(search_eliminate) is None:
            messagebox.showinfo('Error', 'No student found with that ID.')
            return

        # Eliminar los registros relacionados en la tabla Grades
        consulta_delete_grades = 'DELETE FROM Grades WHERE Id_student = %s'
        cursor.execute(consulta_delete_grades, (search_eliminate,))
        conexion.commit()

        # Ahora eliminar el estudiante de la tabla Student
        consulta_delete_student = 'DELETE FROM Student WHERE Id_student = %s'
        cursor.execute(consulta_delete_student, (search_eliminate,))
        conexion.commit()

        messagebox.showinfo('Deleted', f'Student with ID {search_eliminate} has been eliminated.')


# Create the main window
root = tk.Tk()
root.title("Student Management System")

# Create an instance of the Student class
school_students = Student()

# Create the buttons and link them to the corresponding functions
login_button = tk.Button(root, text="Login Student", command=lambda: login_student())
login_button.pack(pady=10)

view_button = tk.Button(root, text="View Students", command=lambda: view_students())
view_button.pack(pady=10)

update_button = tk.Button(root, text="Update Student", command=lambda: update_student())
update_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Student", command=lambda: delete_student())
delete_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Create a treeview widget (table) to display the students
tree = ttk.Treeview(root, columns=("ID Student", "First Name", "Last Name", "Year"), show="headings")
tree.heading("ID Student", text="ID Student")
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Year", text="Year")

# Hide the treeview initially
tree.pack_forget()

# Functions to call each method from Student class
def login_student():
    school_students.login_students()
    school_students.list_dates_student()

def view_students():
    school_students.builder()
    school_students.view_dates_students()
    tree.pack(pady=10)  # Show the table when the button is pressed

def update_student():
    school_students.update_students()

def delete_student():
    school_students.eliminate_student()

# Run the Tkinter main loop
root.mainloop()
