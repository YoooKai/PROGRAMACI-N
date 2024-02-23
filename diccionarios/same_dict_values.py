# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    #all_same = True
    #first_value = list(items.values())[0] if items else None;
    #for value in list(items.values())[1:]:
        #if value != first_value:
            #all_same =  False
            #break
    all_same = False
    if not items:
        all_same = True
    unique_values = set(items.values())
    if len(unique_values) == 1:
        all_same = True



    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})