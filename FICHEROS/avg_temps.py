# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    with open(input_path, 'r') as file:
        with open(output_path, 'w') as output_file:
            for line in file:
                splitted = line.split(',')
                num_elementes = len(splitted)
                addition = 0
                for num in splitted:
                    addition += int(num.strip())
                media = round(addition / num_elementes, 2)
                output_file.write(str(media) + '\n')

    return filecmp.cmp(output_path, 'data\avg_temps\.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')
