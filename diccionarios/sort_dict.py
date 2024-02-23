# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    # recorrer diccionario, los valores orden sort y meter clave como tupla? das = (as, ad)
    sorted_items = []
    item_values = []
    item_keys = []
    for key, value in unsorted_items.items():
        item_keys.append(key)
        item_values.append(value)

    sorted_values = sorted(item_values)
    for value in sorted_values:
        key = item_keys[item_values.index(value)]
        sorted_items.append((key, value))

    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})
