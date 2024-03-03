# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def factorial(number):
    result = 1
    for i in range(number, 1, -1):
        result *= i
    return result


print(factorial(3))
