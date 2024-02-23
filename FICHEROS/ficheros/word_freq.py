# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    unfiltered_freq = {}
    with open(input_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in unfiltered_freq:
                    unfiltered_freq[word] += 1
                else:
                    unfiltered_freq[word] = 1
    freq = {}
    for key, value in unfiltered_freq.items():
        if value >= lower_bound:
            freq[key] = value

    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)
