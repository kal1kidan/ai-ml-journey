# Lesson 2: Functions + Booleans + Conditionals
#
# Functions allow us to create reusable blocks of code.
# Conditionals allow our programs to make decisions.


# -----------------------------------
# Challenge 1:
# How can we create a function that
# receives information and returns a result?
# -----------------------------------

def greet_user(name):
    return f"Hello, {name}!"


print(greet_user("Kal"))
print(greet_user("Sara"))


# -----------------------------------
# Challenge 2:
# How can a function perform a calculation
# and return the answer?
# -----------------------------------

def calculate_circle_area(radius):
    pi = 3.14
    return pi * radius ** 2


area = calculate_circle_area(5)

print("Circle area:", area)


# -----------------------------------
# Challenge 3:
# How do default parameters work?
# What happens if we don't provide a value?
# -----------------------------------

def welcome_user(name="User"):
    return f"Welcome, {name}!"


print(welcome_user())
print(welcome_user("Kal"))


# -----------------------------------
# Challenge 4:
# How can functions make decisions
# using booleans and conditionals?
# -----------------------------------

def check_age(age):

    if age >= 18:
        return "You are allowed to enter."
    else:
        return "You are not allowed to enter."


print(check_age(21))
print(check_age(15))


# -----------------------------------
# Challenge 5:
# Can we build a simple prediction system?
#
# Input:
# Number of hours studied
#
# Output:
# Prediction message
# -----------------------------------

def predict_success(hours_studied):

    if hours_studied >= 5:
        return "High chance of success"
    else:
        return "Need more practice"


print(predict_success(7))
print(predict_success(2))


# -----------------------------------
# Challenge 6:
# How can functions work together?
# -----------------------------------

def calculate_score(correct_answers, total_questions):

    return (correct_answers / total_questions) * 100


def evaluate_score(score):

    if score >= 80:
        return "Excellent performance"
    elif score >= 50:
        return "Good performance"
    else:
        return "Keep practicing"


student_score = calculate_score(8, 10)

print("Score:", student_score)
print(evaluate_score(student_score))