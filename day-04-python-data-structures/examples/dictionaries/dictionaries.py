# Creating a dictionary
student = {
    "name": "Abebe",
    "age": 20,
    "grade": "A"
}

# Accessing a value
print("Student name:", student["name"])

# Adding a new key-value pair
student["school"] = "XYZ University"

# Updating a value
student["grade"] = "A+"

# Printing all keys
print("\nKeys:")
for key in student.keys():
    print(key)

# Printing all values
print("\nValues:")
for value in student.values():
    print(value)

# Printing key-value pairs
print("\nStudent Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Using get()
print("\nCity:", student.get("city", "Not found"))

# Dictionary of books
books = {
    "Atomic Habits": 320,
    "Deep Work": 296,
    "The Psychology of Money": 256
}

# Print all book titles
print("Book Titles:")
for title in books.keys():
    print(title)

# Print all page counts
print("\nPage Counts:")
for pages in books.values():
    print(pages)

# Add a new book
books["Rich Dad Poor Dad"] = 336

# Update a page count
books["Atomic Habits"] = 350

# Find the book with the most pages
max_book = max(books, key=books.get)

print(f"\nBook with the most pages: {max_book} ({books[max_book]} pages)")

# Check if a book exists
print("\nIs 'Deep Work' in the dictionary?")
print("Deep Work" in books)

# Print all books
print("\nLibrary:")
for title, pages in books.items():
    print(f"{title} -> {pages} pages")