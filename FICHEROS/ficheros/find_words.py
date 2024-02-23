# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    with open(data_path, 'r') as file:
        line_number = 0
        for line in file:
            line_number += 1
            char_count = 0
            while True:
                index = line[char_count:].lower().find(target_word.lower())
                if index == -1:
                    break
                char_count += index + len(target_word)
                if (
                    char_count - len(target_word) == 0
                    or not line[char_count - len(target_word) - 1].isalnum()
                ):
                    if char_count == len(target_word) or not line[char_count].isalnum():
                        matches.append((line_number, char_count - len(target_word)))

    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')
