# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n):
    """
    A function that gets an n parameter and includes a generator expression to calculate the first n positive squared numbers.
    :param n: the limit number
    :type n: integer

    :return: result
    :type: list

    """
    return list(num**2 for num in range(n))
    # result = list(num**2 for num in range(n))
    # return result
