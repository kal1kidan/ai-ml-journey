try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    result = first_number / second_number

except ValueError:
    print("Invalid input. Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Result:", result)
    print("Division completed successfully.")

finally:
    print("Program finished.")