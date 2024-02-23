# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = 'data/sum_matrix/result.dat'
    with open(matrix1_path, 'r') as file1, open(matrix2_path, 'r') as file2, open(
        result_path, 'w'
    ) as output_file:
        for line1, line2 in zip(file1, file2):
            nums1 = [int(num) for num in line1.split()]
            nums2 = [int(num) for num in line2.split()]
            for num1, num2 in zip(nums1, nums2):
                addition = f'{num1 + num2} '
                output_file.write(addition)
            output_file.write('\n')

    return filecmp.cmp(result_path, 'data\sum_matrix\.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')
