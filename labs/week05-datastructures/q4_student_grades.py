# Q4: Store a student's courses and grades
# Author: Sophie

student = {
    "name": "Mary",
    "modules": [
        {"courseName": "Programming", "grade": 45},
        {"courseName": "History", "grade": 99},
    ]
}

print(f"Student: {student['name']}")
for module in student["modules"]:
    print("\t{}:\t{}".format(module["courseName"], module["grade"]))