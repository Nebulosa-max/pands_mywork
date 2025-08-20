import json

FILENAME = "students.json"

def save_students(students):
    """Save the list of students to a JSON file."""
    with open(FILENAME, 'w') as f:
        json.dump(students, f)

def load_students():
    """Load the list of students from a JSON file."""
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def do_load():
    """Load students and return the list."""
    return load_students()

def display_menu():
    """Display the menu options and return the user's choice."""
    print("\nWhat would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    return input("Type one letter (a/v/s/l/q): ").strip().lower()

def add_student(students):
    """Add a new student to the list."""
    name = input("Enter student name: ").strip()
    if name:
        students.append(name)
        print(f"Added: {name}")
    else:
        print("No name entered. Student not added.")

def view_students(students):
    """Display the list of students."""
    if not students:
        print("No students found.")
        return
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")

def main():
    """Main program loop."""
    students = []
    while True:
        choice = display_menu()

        if choice == 'a':
            add_student(students)
        elif choice == 'v':
            view_students(students)
        elif choice == 's':
            save_students(students)
            print(f"Students saved to {FILENAME}")
        elif choice == 'l':
            students = do_load()
            print(f"Loaded {len(students)} students from {FILENAME}")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Please select either a, v, s, l, or q.")

if __name__ == "__main__":
    main()
    