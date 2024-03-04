# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(number):
    result = 1
    if number < 0:
        return None
    for i in range(number, 1, -1):
        result *= i
    return result
