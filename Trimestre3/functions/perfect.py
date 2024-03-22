# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n):
    dividers = []
    for num in range(1, n):
        if n % num == 0:
            dividers.append(num)
    return sum(dividers) == n
