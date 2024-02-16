# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    # debenn salir tuplas con num de línea y columna
    # es decir, (41, 23)
    # el num de línea es contando las líneas
    # el num de columna es contando caracteres
    matches = []
    with open(data_path, 'r') as file:
        line_number = 0
        char_count = 0
        for line in file:
            line_number += 1
            char_count = 0
            while target_word in line[char_count]:
                char_count += line[char_count:].index(target_word) + len(target_word)
                matches.append((line_number, char_count))

    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')
