import math_operations


print(math_operations.add(10, 5))
print(math_operations.subtract(10, 5))
print(math_operations.multiply(10, 5))

try:
    print(math_operations.divide(10, 0))
except ValueError as error:
    print(error)