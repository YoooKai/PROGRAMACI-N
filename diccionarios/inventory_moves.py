# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    movements = imoves.split(',')
    for movement in movements:
        article, quantity = movement[0], int(movement[1:])
        inventory[article] = inventory.get(article, 0) + quantity

    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')
