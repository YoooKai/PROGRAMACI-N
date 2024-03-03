# verificar si n está en un rando
def is_in_range(min_val, max_value, n):
    return min_val <= n <= max_value
    #  otro enfoque: if n in range(3, 9):


print(is_in_range(3, 24, 32))
