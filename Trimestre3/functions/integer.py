# def to_square(x):
#    y = x**2
#    return y
#
#
# def calc_area(base, height):
#    area = base * height
#    return area
#


# def f_range(start, end, step=1):
#    pieces = []
#    current = start
#    while current <= end:
#        pieces.append(current)
#        current += step
#    return pieces
#


def integral(start, end, step=1):
    pieces = []
    current = start
    while current <= end:
        pieces.append(current)
        current += step
    result_integer = 0
    for x in pieces:
        y = x**2
        area = y * step
        result_integer += area
    return result_integer


print(integral(0, 2, 0.0001))
