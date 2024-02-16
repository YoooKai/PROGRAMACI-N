# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile, 'r') as file:
        # Obtener las claves desde la primera línea
        data_keys = file.readline().strip().split(',')

        for line in file:
            # Obtener los valores de la línea y dividirlos
            data_values = []
            for value in line.strip().split(','):
                value = value.strip()
                if value == 'True':
                    data_values.append(1)
                elif value == 'False':
                    data_values.append(0)
                elif value.isdigit():
                    data_values.append(int(value))
                else:
                    data_values.append(value)

            # Crear un diccionario con las claves y valores y agregarlo a la lista
            dictionary = dict(zip(data_keys, data_values))
            data.append(dictionary)

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')
