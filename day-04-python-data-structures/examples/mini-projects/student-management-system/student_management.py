students = {
    "kal": {
        "age": 20,
        "grade": "A",
        "email": "kal@example.com",
        "department": "Computer Science",
        "marks": [85, 90, 78, 92]
    },

    "john": {
        "age": 22,
        "grade": "B",
        "email": "john@example.com",
        "department": "Mathematics",
        "marks": [88, 94, 82, 90]
    }
}


def display_students():
    print("\nAvailable Students:")
    for student in students:
        print("-", student)


def view_student(name):
    name = name.lower()

    if name in students:
        student = students[name]

        print("\nStudent Details")
        print("----------------")
        print("Name:", name)
        print("Age:", student["age"])
        print("Grade:", student["grade"])
        print("Email:", student["email"])
        print("Department:", student["department"])
        print("Marks:", student["marks"])

        average = sum(student["marks"]) / len(student["marks"])

        print("Average Marks:", average)

    else:
        print("Student not found.")


display_students()

search = input("\nEnter student name: ")

view_student(search)