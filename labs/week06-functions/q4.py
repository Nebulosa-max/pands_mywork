students = []

def readModules():
    # for now, just return empty list
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

# test
doAdd(students)
doAdd(students)
print(students)