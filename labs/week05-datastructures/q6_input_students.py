# Read multiple students. Blank student name stops.
# Each student: any number of modules + grades (blank module stops that student).

def read_grade(prompt="Enter grade (0-100): "):
    while True:
        txt = input(prompt).strip()
        try:
            g = float(txt)
        except ValueError:
            print("Please enter a number.")
            continue
        if 0 <= g <= 100:
            return g
        print("Grade must be between 0 and 100.")

def read_student():
    name = input("Student name (blank to finish all): ").strip()
    if name == "":
        return None
    modules = []
    print("  Enter module names (blank to finish this student).")
    while True:
        mod = input("  Module name: ").strip()
        if mod == "":
            break
        grade = read_grade("  Enter grade (0-100): ")
        modules.append({"courseName": mod, "grade": grade})
    return {"name": name, "modules": modules}

def main():
    all_students = []
    while True:
        student = read_student()
        if student is None:
            break
        all_students.append(student)

    # Print summary of all students
    print("\nSummary\n-------")
    if not all_students:
        print("(No students entered)")
        return

    for s in all_students:
        print(f"Student: {s['name']}")
        if not s["modules"]:
            print("  (No modules)")
        else:
            for m in s["modules"]:
                print(f"  {m['courseName']:<15} : {m['grade']:.0f}")
        print()

if __name__ == "__main__":
    main()