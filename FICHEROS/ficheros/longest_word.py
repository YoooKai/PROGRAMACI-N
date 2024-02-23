# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    with open(input_path, 'r') as file:
        text = file.read()
        words = [word.strip(',.():;') for word in text.split()]
        max_len = max(len(word) for word in words)
        for word in words:
            if len(word) == max_len:
                longest_word = word

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')
