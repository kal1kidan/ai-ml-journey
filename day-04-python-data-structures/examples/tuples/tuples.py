# Creating a tuple
student = ("Kal", 21, "Software Engineering", "AAU")

# Accessing elements
print("Name:", student[0])
print("University:", student[-1])

# Slicing
print("First three values:", student[:3])

# Length
print("Number of items:", len(student))

# Loop through the tuple
print("\nStudent Information:")
for item in student:
    print(item)

# Tuple unpacking
name, age, major, university = student

print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("Major:", major)
print("University:", university)

# Sales tuple
sales = (1200, 1500, 1700, 900, 2100)

print("\nSales Statistics")
print("Highest sale:", max(sales))
print("Lowest sale:", min(sales))
print("Total sales:", sum(sales))
print("Average sale:", sum(sales) / len(sales))
print("First three months:", sales[:3])