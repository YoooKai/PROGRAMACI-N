# *************************
# OBTENIENDO LOS BIESTABLES
# *************************


def is_bistable(num: int) -> bool:
    bin_num = bin(num)[2:]
    zeros = bin_num.count('0')
    ones = bin_num.count('1')
    return zeros == ones


def run(a: int, b: int) -> list:
    return [v for v in range(a, b + 1) if is_bistable(v)]


if __name__ == '__main__':
    run(0, 40)
