# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/common_words/output.txt'
    # Leer el archivo de entrada
    with open(input_path, 'r') as file:
        lineas = file.readlines()

        # Calcular el número de palabras comunes entre cada combinación de líneas
        resultados = []

        # Recorremos cada línea del archivo
        for linea1 in lineas:
            # Comparamos con cada otra línea
            for linea2 in lineas:
                # Convertir las líneas a minúsculas y dividirlas en palabras
                palabras1 = set(linea1.lower().split())
                palabras2 = set(linea2.lower().split())

                # Calcular el número de palabras comunes
                resultado = len(palabras1.intersection(palabras2))

                # Agregar el resultado a la lista de resultados
                resultados.append(resultado)

        # Escribir los resultados en el archivo de salida
        with open(output_path, 'w') as output_file:
            for resultado in resultados:
                output_file.write(f'{resultado}\n')

    return filecmp.cmp(output_path, 'data\common_words\.expected', shallow=False)


if __name__ == '__main__':
    run('data/common_words/minizen.txt')
