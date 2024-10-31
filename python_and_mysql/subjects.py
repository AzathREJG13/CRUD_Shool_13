class Subject:
    def __init__(self):
        self.subject = {
            101: 'Chemistry_1', 201: 'Chemistry_2', 301: 'Chemistry_3',
            102: 'Math_1', 202: 'Math_2', 302: 'Math_3',
            103: 'Language_1', 203: 'Language_2', 303: 'Language_3',
            104: 'Physics_1', 204: 'Physics_2', 304: 'Physics_3'
        }
        self.list_subjects = []

    def search_for_year(self):
        while True:
            try:
                subject_year = int(input('Please enter the school year (1, 2, or 3): '))
                if subject_year not in [1, 2, 3]:
                    print('Invalid entry. Only 1, 2, or 3 are valid school years.')
                else:
                    start_id = 100 * subject_year + 1
                    end_id = start_id + 3
                    self.list_subjects = [self.subject.get(i) for i in range(start_id, end_id + 1)]
                    print(f'Subjects for {subject_year}{"st" if subject_year == 1 else "nd" if subject_year == 2 else "rd"} year: {self.list_subjects}')
                    self.list_subjects.clear()
                    break
            except ValueError:
                print('Error: Please enter a number for the school year.')

    def search_one_subject(self):
        while True:
            try:
                subject_id = int(input('Enter subject ID: '))
                subject = self.subject.get(subject_id)
                if subject is None:
                    print('Subject ID not found.')
                else:
                    print(f'Subject: {subject}')
                    break
            except ValueError:
                print('Error: Please enter a valid numeric ID.')

    def all_subjects(self):
        print("All subjects and their IDs:")
        for id, name in self.subject.items():
            print(f"{id}: {name}")
    
    def search_subject_for_class(self):
        while True:
            subject_class = input('Enter C (Chemistry), P (Physics), L (Language), M (Math): ').lower()
            if subject_class in ['c', 'p', 'l', 'm']:
                start_id = {'c': 101, 'p': 104, 'l': 103, 'm': 102}[subject_class]
                self.list_subjects = [self.subject.get(i) for i in range(start_id, start_id + 400, 100)]
                class_name = {'c': 'Chemistry', 'p': 'Physics', 'l': 'Language', 'm': 'Math'}[subject_class]
                print(f'Subjects for {class_name}: {self.list_subjects}')
                self.list_subjects.clear()
                break
            else:
                print('Invalid entry. Please choose a valid class option.')

my_subject = Subject()

while True:
    option = input('Enter: Y (search for year), O (search for one subject), A (all subjects), C (search by class), X (exit): ').lower()

    if option == 'y':
        my_subject.search_for_year()
    elif option == 'o':
        my_subject.search_one_subject()
    elif option == 'a':
        my_subject.all_subjects()
    elif option == 'c':
        my_subject.search_subject_for_class()
    elif option == 'x':
        print('Exiting...')
        break
    else:
        print('Invalid option. Please enter a valid choice.')
