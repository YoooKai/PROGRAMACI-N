# *******************
# EXTRACCIÓN DE PARES
# *******************


def run(values):
    evens = []
    for value in values:
        if value % 2 == 0:
            evens.append(value)
    return evens
