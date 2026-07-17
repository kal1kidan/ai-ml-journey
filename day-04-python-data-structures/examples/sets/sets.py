# Creating a set
students = {
    "Kal",
    "Sara",
    "John",
    "Kal",
    "David"
}

print("Students:", students)

# Add a student
students.add("Abebe")

# Remove a student
students.discard("John")

# Check membership
print("\nIs Sara in the set?", "Sara" in students)

# Number of students
print("Total students:", len(students))

# Loop through the set
print("\nStudent List:")
for student in students:
    print(student)

# Set operations
python_students = {"Kal", "Sara", "John"}
ml_students = {"Sara", "David", "Kal"}

print("\nUnion:", python_students | ml_students)
print("Intersection:", python_students & ml_students)
print("Difference:", python_students - ml_students)
print("Symmetric Difference:", python_students ^ ml_students)

# Bonus
visitors = [
    "Kal",
    "Sara",
    "John",
    "Kal",
    "David",
    "Sara",
    "Kal"
]

unique_visitors = set(visitors)

print("\nUnique visitors:", unique_visitors)
print("Number of unique visitors:", len(unique_visitors))
print("Did Abebe visit?", "Abebe" in unique_visitors)