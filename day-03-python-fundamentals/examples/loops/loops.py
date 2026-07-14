'''sales = [1200, 1500, 900, 2000, 1700]

# Print each sale
for sale in sales:
    print(sale, end=" ")

print()

# Calculate total sales
total_sales = 0

for sale in sales:
    total_sales += sale

print("Total sales:", total_sales)

# Calculate average
average_sales = total_sales / len(sales)

print("Average sales:", average_sales)

# Find highest sale
highest_sale = max(sales)

print("Highest sale:", highest_sale)

# Filter sales above 1500 using list comprehension
sales_above_1500 = [
    sale for sale in sales 
    if sale > 1500
]

print("Sales above 1500:", sales_above_1500)'''
text = "Python is powerful and Python is easy to learn"

words = text.split()

# Count words
count = 0

for word in words:
    count += 1

print("Number of words:", count)

# Print words
for word in words:
    print(word, end=" ")

print()

# Count occurrences of Python
count_python = 0

for word in words:
    if word == "Python":
        count_python += 1

print("Number of times 'Python' appears:", count_python)

# Words longer than 5 letters
long_words = []

for word in words:
    if len(word) > 5:
        long_words.append(word)

print("Words longer than 5 letters:", long_words)