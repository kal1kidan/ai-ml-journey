# Lesson 1: Arithmetic Operations in Python

# -----------------------------------
# Basic Arithmetic Operations
# -----------------------------------

number_a = 15
number_b = 4

print("Addition:", number_a + number_b)
print("Subtraction:", number_a - number_b)
print("Multiplication:", number_a * number_b)
print("Division:", number_a / number_b)
print("Floor Division:", number_a // number_b)
print("Remainder:", number_a % number_b)
print("Power:", number_a ** number_b)


# -----------------------------------
# Question 1:
# What is the difference between normal division
# and floor division?
# -----------------------------------

profit = 1000
shareholders = 7

normal_division = profit / shareholders
floor_division = profit // shareholders

print("Normal division:", normal_division)
print("Floor division:", floor_division)

# Normal division keeps decimal values.
# Floor division removes the decimal part.


# -----------------------------------
# Question 2:
# How can we find the remainder after division?
# -----------------------------------

items = 100
groups = 3

remaining_items = items % groups

print("Remaining items:", remaining_items)

# % gives the remainder after division.


# -----------------------------------
# Question 3:
# How do we calculate a number raised to a power?
# -----------------------------------

radius = 5

area = 3.14 * (radius ** 2)

print("Circle area:", area)

# ** is the exponent operator.


# -----------------------------------
# Question 4:
# What happens when arithmetic operators
# are used with different data types?
# -----------------------------------

integer_number = 10
decimal_number = 2.5

result = integer_number + decimal_number

print("Integer + Float:", result)
print("Result type:", type(result))

# Python converts the integer into a float.


# -----------------------------------
# Question 5:
# What happens when we add two strings?
# -----------------------------------

first_word = "AI"
second_word = "Engineer"

combined = first_word + " " + second_word

print(combined)

# + joins strings together (concatenation).


# -----------------------------------
# Question 6:
# What happens when we multiply a string
# by an integer?
# -----------------------------------

message = "Python "

print(message * 3)

# Python repeats the string.


# -----------------------------------
# Question 7:
# What happens when we use booleans
# in arithmetic?
# -----------------------------------

true_value = True
false_value = False

print(true_value + true_value)
print(false_value + 5)

# True behaves like 1 and False behaves like 0.


# -----------------------------------
# Question 8:
# Useful built-in numerical functions
# -----------------------------------

numbers = [10, 25, 5]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Absolute value:", abs(-20))


# -----------------------------------
# Question 9:
# Does Python always return the same
# data type after calculations?
# -----------------------------------

division_result = 10 / 2
floor_result = 10 // 2

print(type(division_result))
print(type(floor_result))