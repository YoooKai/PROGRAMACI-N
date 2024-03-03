# multiplicar elementos de una lista
def mult_values(values):
    result = 1
    for value in values:
        result *= value
    return result


print(mult_values([2, 3, 2]))
