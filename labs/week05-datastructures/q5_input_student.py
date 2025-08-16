# Read one student's name, then any number of modules+grades (stop on blank),
# then print a neat summary.

def read_nonempty(prompt):
    """Read a non-empty string (but allow blank when caller wants to stop)."""
    s = input(prompt)
    return s

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

def main():
    student_name = input("Student name: ").strip()
    if student_name == "":
        print("No student entered. Goodbye.")
        return

    modules = []
    print("Enter module names (blank to finish).")
    while True:
        mod = read_nonempty("Module name: ").strip()
        if mod == "":
            break
        grade = read_grade()
        modules.append({"courseName": mod, "grade": grade})

    # Print summary
    print(f"\nStudent: {student_name}")
    if not modules:
        print("  (No modules entered)")
    else:
        for m in modules:
            # tidy align (course left, grade right)
            print(f"  {m['courseName']:<15} : {m['grade']:.0f}")

if __name__ == "__main__":
    main()