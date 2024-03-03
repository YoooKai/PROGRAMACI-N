def maxoftwo(num1, num2):
    if num1 > num2:
        return num1
    return num2


def maxofthree(num1, num2, num3):
    max = maxoftwo(num1, num2)
    max = maxoftwo(max, num3)
    return max


print(maxofthree(34, 39, 23))
