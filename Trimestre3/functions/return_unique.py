# recibe una lista y devuelve lista con solo caracteres únicos
def unique_items(items):
    result = list(set(items))
    return result


example = [3, 3, 4, 65, 6, 4, 3, 4, 5, 5]
print(unique_items(example))

# otra manera es comprobando elemento por elemento y si restá en una nueva lista, no añadir, si no, añadir
