# q7_view.py

def displayModules(modules):
    print("\nName\t\tGrade")
    for module in modules:
        # use single quotes inside the f-string (fixes the “quotes inside quotes” hint)
        print(f"\t{module['name']:<15}\t{module['grade']:>3}")

def doView(students):
    # print each student and their modules nicely
    print("\nSummary")
    for s in students:
        print(f"\nStudent: {s['name']}")
        if not s['modules']:
            print("\t(No modules)")
        else:
            displayModules(s['modules'])


# --- tiny demo so you can run this file by itself ---
if __name__ == "__main__":
    demo_students = [
        {"name": "Bruna", "modules": [{"name": "Maths", "grade": 78}, {"name": "Programming", "grade": 99}]},
        {"name": "Mary",  "modules": []}
    ]
    doView(demo_students)