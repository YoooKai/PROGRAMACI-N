# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:
    # Inicialización de variables
distance = 0
depth = 0
fuel = 0

# Lectura del archivo
with open(route_path, 'r') as file:
    # Iterar sobre cada línea del archivo
    for line in file:
        # Verificar si la línea contiene información sobre el combustible
        if line.startswith('<'):
            # Obtener la cantidad de combustible
            fuel = int(line[1:])
        else:
            # La línea contiene movimientos, procesar cada movimiento
            movements = line.strip().split(',')
            for movement in movements:
                # Dividir el movimiento en componentes x e y sin usar map
                x, y = [int(coord) for coord in movement.split(':')]
                
                # Actualizar la distancia y la profundidad
                distance += x
                depth += y
                
                # Verificar condiciones de parada
                if fuel <= 0 or depth == 0 or depth == 600:
                    break

                # Restar el combustible consumido durante el movimiento
                fuel -= (3 * abs(x) + 2 * abs(y))
                
                # Verificar si el combustible se ha agotado
                if fuel <= 0:
                    break

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')
