# ------------GENERADORES--------------------------
# Permiten extraer valores de una función y almacenarlos d euno en uno en objetos iterables
# que se pueden recorrer sin tneer que almacenarlos todos a la vez.

# Versión función normal múltiplos


def genera_mult7(limite):
    num = 1
    lista_num = []
    while num <= limite:
        lista_num.append(num * 7)
        num += 1
        return lista_num


genera_mult7(32)

# versión generadora


def genera_mult8(limite):
    num = 1
    while num <= limite:
        yield num * 8
        num += 1


def print_samples():
    for n in genera_mult8:
        print(n)
