# Write a Python function to find the maximum of three numbers.
def calculatemax(number):
    maxnum = number[0]
    for num in number:
        if num > maxnum:
            maxnum = num

    return maxnum


cadena = [3, 6, 46, 33, 99, 66]
print(calculatemax(cadena))
