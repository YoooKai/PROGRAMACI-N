# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors
# other than 1 and itself.
def is_prime(num):
    for i in range(2, num):
        if num < 2:
            return False
        elif num % i == 0:
            return False
    return True


print(is_prime(2))
