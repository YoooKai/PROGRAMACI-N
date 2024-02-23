# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    counted_lines = 0
    with open(input_path, 'r') as file:
        for line in file:
            if line_no <= 0 or line == '':
                line = None
            else:
                line = line.strip()
                counted_lines += 1
                if counted_lines == line_no:
                    break

    return line


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)
