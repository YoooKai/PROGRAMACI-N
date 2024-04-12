# ejercicios

# cycle_alphabet

# *****************
# ALFABETO CIRCULAR
# *****************


def get_alphabet(num_letters: int):
    for num in range(num_letters):
        yield num


def run(max_letters: int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text = ''
    for num in get_alphabet(max_letters):
        text += ALPHABET[num % len(ALPHABET)]
    return text


# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list[int]) -> list[int]:
    items_length = len(items)
    items_copy = items.copy()
    for round in range(items_length - 1):
        for index in range(items_length - 1 - round):
            if items_copy[index] > items_copy[index + 1]:
                buffer = items_copy[index + 1]
                items_copy[index + 1] = items_copy[index]
                items_copy[index] = buffer
    return items_copy


# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(
    items: list[int], target_count: int, counter: int = 1, previous_num: int = 0
) -> int:
    if len(items) > 0:
        if items[0] == previous_num:
            if counter == target_count:
                return items[0]
            return consecutive_seq(
                items[1:], target_count, counter=counter + 1, previous_num=items[0]
            )
        else:
            return consecutive_seq(items[1:], target_count, counter=1, previous_num=items[0])
    else:
        return False

    # ***************


# CUADRADO MÁGICO
# ***************


def sum_rows(matrix: list[int]) -> list[int]:
    result = [sum(row) for row in matrix]
    return result


def sum_columns(matrix: list[int]) -> list[int]:
    matrix_lenght = len(matrix) - 1
    result = [0 for _ in range(matrix_lenght)]
    for row in matrix:
        for col_index in matrix_lenght:
            result[col_index] += row[col_index]
    return result


def sum_diagonals(matrix: list[int]) -> list[int]:
    first_diagonal = sum([])
    return result


def is_magic_square(values: list[int]) -> bool:
    pass


# *******************
# FIBONACCI RECURSIVO
# *******************


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# **************
# HIPERFACTORIAL
# **************


def hyperfactorial(n: int) -> int:
    return 1 if n <= 1 else (n**n) * hyperfactorial(n - 1)


# *******************
# FIBONACCI GENERADOR
# *******************


def fibonacci_gen(n: int):
    for num in range(1, n):
        if num == 0:
            yield 0
        elif num == 1:
            yield 1
        else:
            yield (num - 1) + (num - 2)


def run(n: int) -> list[int]:
    return list(fibonacci_gen(n))

    # ********************


# MÁXIMO COMÚN DIVISOR
# ********************


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


# o
def gcd_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


# *******************************
# ASEGURANDO ARGUMENTOS POSITIVOS
# *******************************


def assert_positive(func):
    def wrapper(*args, **kwargs):
        # Verificar los argumentos posicionales
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return 0
        # Verificar los argumentos nominales
        for kwarg, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                return 0
        # Llamar a la función original si todos los argumentos son positivos
        return func(*args, **kwargs)

    return wrapper


@assert_positive
def factorial(n: int) -> int:
    if n == 0:  # Caso base: factorial de 0 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva: n * factorial(n - 1)
