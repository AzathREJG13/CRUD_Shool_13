from mysql_conexion import cursor, conexion

class Subject:
    def __init__(self):
        self.subject = {}
        self.list_subject = []
        self.name = None
        self.id_subject = None
    
    def builder(self):
        consulta = 'SELECT * FROM Subjects'
        cursor.execute(consulta)
        result = cursor.fetchall()
        for i in result:
            self.id_subject = i[0]
            self.name = [i[1]]
            self.subject[self.id_subject] = self.name
        print("Subjects loaded from database:", self.subject)
        
    def serch_for_year(self):
        while True:
            try:
                year = int(input("Enter the year of study (1, 2, or 3): "))
                if year == 1:
                    for i in range(101, 105, 1):
                        serch_subject = self.subject.get(i)
                        self.list_subject.append(serch_subject)
                    print("Subjects for Year 1:", self.list_subject)
                    self.list_subject.clear()
                    break
                elif year == 2:
                    for i in range(201, 205, 1):
                        serch_subject = self.subject.get(i)
                        self.list_subject.append(serch_subject)
                    print("Subjects for Year 2:", self.list_subject)
                    self.list_subject.clear()
                    break   
                elif year == 3:
                    for i in range(301, 305, 1):
                        serch_subject = self.subject.get(i)
                        self.list_subject.append(serch_subject)
                    print("Subjects for Year 3:", self.list_subject)
                    self.list_subject.clear()
                    break        
                else:
                    print("Invalid year. Please enter 1, 2, or 3.")
            except ValueError:
                print("Input error. Please enter a valid year (numeric).")
                
    def search_for_branch(self):
        while True:
            branch = input("Enter the branch (C for Chemistry, M for Math, P for Physics, L for Language): ").lower()
            if branch == 'c':
                for i in range(101, 401, 100):
                    serch_branch = self.subject.get(i)
                    self.list_subject.append(serch_branch)
                print("Subjects for Chemistry branch:", self.list_subject)
                self.list_subject.clear()
                break
            elif branch == 'm':
                for i in range(102, 402, 100):
                    serch_branch = self.subject.get(i)
                    self.list_subject.append(serch_branch)
                print("Subjects for Math branch:", self.list_subject)
                self.list_subject.clear()
                break
            elif branch == 'p':
                for i in range(103, 403, 100):
                    serch_branch = self.subject.get(i)
                    self.list_subject.append(serch_branch)
                print("Subjects for Physics branch:", self.list_subject)
                self.list_subject.clear()
                break
            elif branch == 'l':
                for i in range(104, 404, 100):
                    serch_branch = self.subject.get(i)
                    self.list_subject.append(serch_branch)
                print("Subjects for Language branch:", self.list_subject)
                self.list_subject.clear()
                break
            else:
                print("Invalid branch. Please enter C, M, P, or L.")
                
    def search_subject_for_one(self):
        while True:
            try:
                search_id = int(input("Enter the subject ID to search: "))
                subject_id = self.subject.get(search_id)
                if subject_id is None:
                    print("Subject not found for the given ID.")
                else:
                    print(f"Subject found: {subject_id}")
                break
            except ValueError:
                print("Input error. Please enter a numeric subject ID.")

if __name__ == "__main__":
    my_subject = Subject()
    my_subject.builder()

    while True:
        opcion = input("Choose an option: Y (Search by year), B (Search by branch), O (Search by subject ID), or X (Exit): ").lower()
        if opcion == 'y':
            my_subject.serch_for_year()
        elif opcion == 'b':
            my_subject.search_for_branch()
        elif opcion == 'o':
            my_subject.search_subject_for_one()
        elif opcion == 'x':
            print("Exiting the program. Closing database connection.")
            cursor.close()
            conexion.close()
            break
        else:
            print("Invalid option. Please enter Y, B, O, or X.")
