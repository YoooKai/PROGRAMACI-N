# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def reverse_str(items):
    rev_string = items[::-1]
    # rev_string = ''.join(reversed(items))
    return rev_string


print(reverse_str('1234abcd'))
