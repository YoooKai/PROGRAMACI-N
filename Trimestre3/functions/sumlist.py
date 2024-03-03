#  Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def add(values):
    result = 0
    for value in values:
        result += value
    return result


print(add([22, 3, 4]))
