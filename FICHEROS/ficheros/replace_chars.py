# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = 'data/replace_chars/r_noticia.txt'

    individual_letters = replacements.split('|')
    target_chars = [letter[0] for letter in individual_letters]
    rep_chars = [letter[1] for letter in individual_letters]
    with open(input_path, 'r') as inputf, open(output_path, 'w') as outputf:
        for line in inputf:
            for target_char, rep_char in zip(target_chars, rep_chars):
                line = line.replace(target_char, rep_char)
            outputf.write(line)

    return filecmp.cmp(output_path, 'data\replace_chars\.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu')
