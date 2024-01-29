# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    first_values = set()
    second_values = set()
    for first, second in input:
        first_values.add(first)
        second_values.add(second)
    output = first_values, second_values

    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
