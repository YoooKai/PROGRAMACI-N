# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def get_even(numbers):
    ev_nums = []
    for num in numbers:
        if num % 2 == 0:
            ev_nums.append(num)
    return ev_nums


sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(get_even(sample))
