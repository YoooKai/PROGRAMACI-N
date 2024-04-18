# *************************************
# CALCULANDO EL MÁXIMO CON RECURSIVIDAD
# *************************************


def rmax(items):
    if len(items) == 1:
        return items[0]
    partial_max = rmax(items[1:])
    return items[0] if items[0] > partial_max else partial_max
