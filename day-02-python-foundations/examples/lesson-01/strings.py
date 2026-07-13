# Lesson 1: Strings in Python
#
# Strings are used to store and work with text.
# This file explores common string operations.


# -----------------------------------
# Question 1:
# How do we create strings in Python?
# Can we use single and double quotes?
# -----------------------------------

message_one = "Hello, World!"
message_two = 'Python is fun'

print(message_one)
print(message_two)


# -----------------------------------
# Question 2:
# How can we combine multiple strings?
# -----------------------------------

greeting = "Hello"
user = "Kal"

full_greeting = greeting + " " + user

print(full_greeting)

# The + operator joins strings together.
# This process is called concatenation.


# -----------------------------------
# Question 3:
# How can we find the number of characters
# inside a string?
# -----------------------------------

greeting_length = len(greeting)

print("Length of greeting:", greeting_length)

# len() counts the characters inside a string.


# -----------------------------------
# Question 4:
# How can we access individual characters
# inside a string?
# -----------------------------------

word = "Python"

first_character = word[0]
middle_character = word[len(word) // 2]
last_character = word[-1]

print("First character:", first_character)
print("Middle character:", middle_character)
print("Last character:", last_character)

# Python indexing starts from 0.
# Negative indexes count from the end.


# -----------------------------------
# Question 5:
# How can we modify strings using methods?
# -----------------------------------

text = "python"

uppercase_text = text.upper()
lowercase_text = text.lower()
replaced_text = text.replace("python", "AI")

print("Uppercase:", uppercase_text)
print("Lowercase:", lowercase_text)
print("Replaced:", replaced_text)

# String methods create modified versions
# without changing the original string.


# -----------------------------------
# Question 6:
# How can we create dynamic sentences
# using variables?
# -----------------------------------

name = "Kal"
favorite_language = "Python"
goal = "become an AI/ML engineer"

profile = f"My name is {name}, my favorite programming language is {favorite_language}, and my goal is to {goal}."

print(profile)

# f-strings allow variables to be inserted
# directly inside a string.


# -----------------------------------
# Question 7:
# How can we check if a word exists
# inside a string?
# -----------------------------------

sentence = "Python is amazing"

contains_python = "Python" in sentence

print("Does the sentence contain Python?", contains_python)

# The 'in' operator checks membership.


# -----------------------------------
# Question 8:
# How can we count how many times
# something appears in a string?
# -----------------------------------

number_of_python = sentence.count("Python")

print("Number of times Python appears:", number_of_python)


# -----------------------------------
# Question 9:
# What happens when we multiply
# a string by an integer?
# -----------------------------------

message = "AI "

print(message * 3)

# Multiplying strings repeats the text.


# -----------------------------------
# Question 10:
# What is the difference between
# concatenation and f-strings?
# -----------------------------------

product = "Laptop"
price = 1200

# Using concatenation
print("The " + product + " costs $" + str(price))

# Using f-string
print(f"The {product} costs ${price}")

# Concatenation requires converting numbers
# into strings using str().
# f-strings handle conversion automatically.


# -----------------------------------
# Question 11:
# How can we check the type of a string?
# -----------------------------------

print(type(product))

# type() tells us the data type of a value.