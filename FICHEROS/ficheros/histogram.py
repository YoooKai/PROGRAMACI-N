# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    with open(data_path, 'r') as inputf:
        rep_count = {}
        content = inputf.read()
        elem_list = list(content)
        for char in elem_list:
            if char in rep_count:
                rep_count[char] += 1
            else:
                rep_count[char] = 1

    sorted_rep_count = dict(sorted(rep_count.items()))
    with open(histogram_path, 'w') as outputf:
        for char, count in sorted_rep_count.items():
            histogram_line = f"{char.upper()} {'█' * count} {count}"
            outputf.write(histogram_line + '\n')

    return filecmp.cmp(histogram_path, 'data\histogram\.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')
