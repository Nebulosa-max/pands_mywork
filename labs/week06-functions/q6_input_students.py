# Lab 06 – Q6: menu + add/view students

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip().lower()
    return choice


def readModules():
    """Return a list like: [{'name':'Prog','grade':45}, ...]"""
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade (0-100): "))
        modules.append(module)
        moduleName = input("\tEnter next Module name (blank to quit): ").strip()
    return modules


def doAdd(students):
    """Read one student (name + modules) and append to the students list."""
    currentStudent = {}
    currentStudent["name"] = input("Enter student name: ").strip()
    currentStudent["modules"] = readModules()
    students.append(currentStudent)


def doView(students):
    """Pretty-print all students and their modules/grades."""
    print("\nSummary")
    if not students:
        print(" (No students entered)")
        return

    for s in students:
        print(f"\nStudent: {s['name']}")
        if not s["modules"]:
            print(" (No modules)")
        else:
            print("Name".ljust(15) + "Grade")
            for m in s["modules"]:
                print(f"{m['name']:<15}{m['grade']:>3}")


def doNothing(dummy):
    pass


def main():
    students = []
    choiceMap = {
        'a': doAdd,
        'v': doView,
        'q': doNothing
    }

    choice = displayMenu()
    while choice != 'q':
        if choice in choiceMap:
            choiceMap[choice](students)
        else:
            print("\nPlease select either a, v or q")

        choice = displayMenu()

    print("Exiting program...")


if __name__ == "__main__":
    main()