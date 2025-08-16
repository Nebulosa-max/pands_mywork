# Lab 06 – Functions
# Q1 to Q3 solutions + (Q4/Q5) add/view students

# ---------- Q1 ----------
def yo(a):
    return a * 2

print("Q1:", yo(3))  # should print 6

# ---------- Q2 ----------
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()
    return choice

# test Q2
choice = displayMenu()
print(f"you chose {choice}")

# ---------- Q4/Q5 ----------
students = []   # store students here (list of dicts)

def doAdd():
    """Read one student + modules and save to 'students'."""
    name = input("enter name: ").strip()
    if not name:
        print("(no name entered)")
        return

    modules = []
    while True:
        mod = input("Module name (blank to finish): ").strip()
        if mod == "":
            break
        grade = int(input("Enter grade (0-100): "))
        modules.append({"courseName": mod, "grade": grade})

    students.append({"name": name, "modules": modules})
    print("Added.\n")

def doView():
    """Print all students currently in 'students'."""
    if not students:
        print("(No students entered)")
        return

    print("\nSummary")
    for s in students:
        print(f"\nStudent: {s['name']}")
        if not s["modules"]:
            print("  (No modules entered)")
        else:
            for m in s["modules"]:
                print(f"  {m['courseName']:<15} {m['grade']:>3}")

# Q3 main loop
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    else:
        print("\nPlease select either a, v, or q")
    # ← always ask again for the next action
    choice = displayMenu()

print("Exiting program...")