# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    with open(text_path, 'r') as givenf:
        with open(md_path, 'w') as outline:
            for line in givenf:
                tab_count = line.count('\t')
                num_pound_signs = '#' * (tab_count + 1)
                outline.write(num_pound_signs + ' ' + line.lstrip('\t'))

    return filecmp.cmp(md_path, 'data\txt2md\.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')
